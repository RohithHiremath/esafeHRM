from django.shortcuts import render
from .models import TardinessDetails
from leaves.models import Holidays
from pim.models import Personal_details
from attendance.models import EmployeeAttendance
import calendar
import datetime
# import xlrd
import openpyxl
# Create your views here.

def policyDetails(request):
    if request.method == 'POST':
        tardinessvalues = TardinessDetails.objects.all()
        if not tardinessvalues:
            tardinessdetails = TardinessDetails(maxallowedlate=request.POST['maxallowedlate'],
                                penalty_late=request.POST['penalty_late'],
                                maxallowedearly=request.POST['maxallowedearly'],
                                penalty_early=request.POST['penalty_early'],
                                holidaycompensatorytype=request.POST['holidaycompensatorytype'],
                                holidaypaymentqty=request.POST['holidaypaymentqty'],
                                weekendcompensatorytype=request.POST['weekendcompensatorytype'],
                                weekendpaymentqty=request.POST['weekendpaymentqty'],
                                holidaydaystoexpire=request.POST['holidaydaystoexpire'],
                                weekenddaystoexpire=request.POST['weekenddaystoexpire'],
                                )
            tardinessdetails.save()
            tardinessvalues = TardinessDetails.objects.all()
            return render(request,'policy.html',{'title':'Attendance Policy Details','tardinessvalues':tardinessvalues})
        else:
            tardinessdetails = TardinessDetails.objects.get(id=1)
            tardinessdetails.maxallowedlate=request.POST['maxallowedlate']
            tardinessdetails.penalty_late=request.POST['penalty_late']
            tardinessdetails.maxallowedearly=request.POST['maxallowedearly']
            tardinessdetails.penalty_early=request.POST['penalty_early']
            tardinessdetails.holidaycompensatorytype=request.POST['holidaycompensatorytype']
            tardinessdetails.holidaypaymentqty=request.POST['holidaypaymentqty']
            tardinessdetails.weekendcompensatorytype=request.POST['weekendcompensatorytype']
            tardinessdetails.weekendpaymentqty=request.POST['weekendpaymentqty']
            tardinessdetails.minimumHoursForOT=request.POST['minimumHoursForOT']
            tardinessdetails.OTcompensatorytype=request.POST['OTcompensatorytype']
            tardinessdetails.OTPayment=request.POST['OTPayment']
            tardinessdetails.holidaydaystoexpire=request.POST['holidaydaystoexpire']
            tardinessdetails.weekenddaystoexpire=request.POST['weekenddaystoexpire']
            tardinessdetails.save()
            tardinessvalues = TardinessDetails.objects.all()
            return render(request,'policy.html',{'title':'Attendance Policy Details','tardinessvalues':tardinessvalues})
    else:
        tardinessvalues = TardinessDetails.objects.all()
        return render(request,'policy.html',{'title':'Attendance Policy Details','tardinessvalues':tardinessvalues})


def shiftDetails(request):
    return render(request,'shiftdetails.html',{'title':'Employee ShiftDetails'})

def uploadattendance(request):
    if "GET" == request.method:
        render(request,'processattendance.html',{'title':'Upload Attendance'})
    else:
        new_file = request.FILES["uploadattendance"]
        wb_obj = openpyxl.load_workbook(new_file)
        sheet_obj = wb_obj.active
        max_row = sheet_obj.max_row
        max_col = sheet_obj.max_column
        # get the attendance date
        cell_obj = sheet_obj.cell(row = 10, column = 6)
        AttendanceDate = cell_obj.value
        AttendanceDate = AttendanceDate.split('-')
        abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}
        AttendanceDate[1] = abbr_to_num[AttendanceDate[1]]
        attendanceMarkingDate = str(AttendanceDate[2])+'-'+str(AttendanceDate[1])+'-'+str(AttendanceDate[0])

        # check if Attendancedate is a holiday
        holiday = Holidays.objects.filter(holidayDate__year= AttendanceDate[2],
                                          holidayDate__month= AttendanceDate[1],
                                          holidayDate__day= AttendanceDate[0])
        if not holiday:
            holidaystatus = 2  # not a holiday
        else:
            holidaystatus = 1  # Its a holiday
        
        leavestatus = 2
        compoffstatus = 2

        for i in range(13, max_row):
            Employee_Code = sheet_obj.cell(row = i, column = 4)
            Employee_Name = sheet_obj.cell(row = i, column = 6)
            shift = sheet_obj.cell(row = i, column = 8)
            Intime = sheet_obj.cell(row = i, column = 9)
            outime = sheet_obj.cell(row = i, column = 10)
            workduration = sheet_obj.cell(row = i, column = 13)
            OT = sheet_obj.cell(row = i, column = 14) 
            totalwork = sheet_obj.cell(row = i, column = 16)
            status = sheet_obj.cell(row = i, column = 17)

            Employee_Code = Employee_Code.value
            Employee_Code = str(Employee_Code).zfill(5)
            Employee_Name = Employee_Name.value
            Employee_shift = shift.value
            Employee_Intime = Intime.value
            Employee_outime = outime.value
            Employee_workduration = workduration.value
            Employee_OT = OT.value
            Employee_totalwork = totalwork.value
            Attendance_status = status.value
            personals = Personal_details.objects.filter(employee_id = Employee_Code).values('id','work_shifts')
            
            emp_id = personals[0]['id']
            emp_shift = personals[0]['work_shifts']

            # if day is not holiday ,check if it is a weekend
            if holidaystatus == 2:
                weekendstatus = 2
            else:
                weekendstatus = 2

            # if employee punch-in time is not available
            if Employee_Intime == '00:00':
                # if not a holiday check if is a weekend
                if holidaystatus == 2:
                    #check for week weekend

                    # if not weekend
                    if weekendstatus == 2:
                        #check for leave
                        if leavestatus == 1:
                            attendancestatus = 4   # Leave
                        else:
                            # check for compoff
                            if compoffstatus == 1:
                                attendancestatus = 5   # Comp Off 
                            else:
                                attendancestatus = 2   # Absent
                    else:
                        attendancestatus = 2   # Absent            
                else:
                    attendancestatus = 2   # Absent
            else:
                if holidaystatus == 1:
                    attendancestatus = 7   # Holiday day present
                else:
                    #check for week weekend
                    if weekendstatus == 1:
                        attendancestatus = 6   # Weekend present
                    else:
                        if Attendance_status == 'P':
                            attendancestatus = 1   # Full day present
                        elif Attendance_status == 'A':
                            attendancestatus = 2   # Absent
                        else:
                            #check if leave 
                            if leavestatus == 1:
                                attendancestatus = 3   # Half day present and half day leave 
                            else:
                                attendancestatus = 8   # Half day present and half day Absent              
            
            attendance_details = EmployeeAttendance(employee_name = Employee_Name,
                                                    employee_shift = Employee_shift,
                                                    employee_intime = Employee_Intime,
                                                    employee_outime = Employee_outime,
                                                    employee_workduration = Employee_workduration,
                                                    employee_OT = Employee_OT,
                                                    employee_totalwork = Employee_totalwork,
                                                    holiday_status = holidaystatus,
                                                    weekend_status = weekendstatus,
                                                    attendance_status = attendancestatus,
                                                    leave_status = leavestatus,
                                                    compoff_status = compoffstatus,
                                                    updated_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                    employee_code_id = emp_id,
                                                    attendance_date = attendanceMarkingDate
                                                    )   
            attendance_details.save()
        AttendanceDate = attendanceMarkingDate.split('-')
        saved_details = EmployeeAttendance.objects.filter( attendance_date__year= AttendanceDate[0],attendance_date__month= AttendanceDate[1],attendance_date__day= AttendanceDate[2]).select_related('employee_code').order_by('employee_code_id')
        return render(request,'processattendance.html',{'title':'Upload Attendance', 'saved_details':saved_details})

    return render(request,'processattendance.html',{'title':'Upload Attendance'})