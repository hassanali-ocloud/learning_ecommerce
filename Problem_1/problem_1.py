from urllib.request import urlopen
import asyncio
from model import TrainReport
from datetime import datetime

async def read_file(url: str):
    try:
        with urlopen(url=url) as response:
            body = response.read().decode('utf-8')
            return body
    except Exception as e:
        print(f"Error fetching the file: {e.reason}")

def convert_to_obj(data: str):
    train_reports = []
    rowDatas = data.split('\n')
    i = 0
    for data in rowDatas:
        if (i==0):
            pass
        else:
            if data == "":
                break
            indvData = data.split(",")
            train_report = TrainReport(indvData[0], indvData[1], indvData[2], indvData[3], indvData[4], indvData[5])
            train_reports.append(train_report)
        i += 1
    return train_reports

def print_total_no_of_incidents(reportLs: list[TrainReport]):
    unique_incident = {}
    for report in reportLs:
        company = report.company
        if company in unique_incident:
            unique_incident[report.company] += 1
        else:
            unique_incident[report.company] = 1
    
    print("Total Num of Incidents for each Railway Company: ")
    for key, val in unique_incident.items():
        print(f"Name: {key} - Num Of Incidents: {val}")

def print_num_of_incidents_in_jan(reportLs: list[TrainReport]):
    jan_incident_num = 0
    for report in reportLs:
        date = report.incident_data
        strip_date = datetime.strptime(date, '%Y-%m-%d').date()
        if strip_date.month == 1:
            jan_incident_num += 1
    
    print(f"Total Num of Incidents reported in Jan: {jan_incident_num}")

def print_train_larget_incidents(reportLs: list[TrainReport]):
    unique_incident = {}
    for report in reportLs:
        train_num = report.train_num
        if train_num in unique_incident:
            unique_incident[report.train_num] += 1
        else:
            unique_incident[report.train_num] = 1

    max_train = max(unique_incident, key=unique_incident.get)
    max_incidents = unique_incident[max_train]  
    print(f"Train with Highest Num of Incidents: {max_train} - {max_incidents}")

def print_days_hours_for_unknown(reportLs: list[TrainReport]):
    print(f"Days & Hours when Unknown Category Incident Happens:")
    for report in reportLs:
        decfect_id = report.defect_id
        if (decfect_id == "42"):
            date = report.incident_data
            time = report.incident_time
            strip_date = datetime.strptime(date, "%Y-%m-%d").date()
            strip_time = datetime.strptime(f"{time}:00", "%H:%M:%S").time()
            print(f"Day: {strip_date.day} & Hour: {strip_time.hour}")

def print_incidents_in_current_month(reportLs: list[TrainReport], today_date: str):
    print(f"Incident Occur on Today's Date: {today_date}")
    today_date = datetime.strptime(today_date, "%Y-%m-%d").date()
    for report in reportLs:
        incident_date = report.incident_data
        strip_date = datetime.strptime(incident_date, "%Y-%m-%d").date()
        if (today_date.month == strip_date.month):
            print(f"Company Name: {report.company} - Train Num: {report.train_num} - Wagon Num: {report.wagon_num}")

async def main():
    url = "https://raw.githubusercontent.com/khuzaima-ocs/railway-incidents/refs/heads/main/rail_incidents.csv"
    data = await read_file(url=url)
    reportLs = convert_to_obj(data)
    print("=========================================================================")
    print_total_no_of_incidents(reportLs)
    print("=========================================================================")
    print_num_of_incidents_in_jan(reportLs)
    print("=========================================================================")
    print_train_larget_incidents(reportLs)
    print("=========================================================================")
    print_days_hours_for_unknown(reportLs)
    print("=========================================================================")
    print_incidents_in_current_month(reportLs, "2022-03-27")
    print("=========================================================================")


if __name__ == "__main__":
    asyncio.run(main())

# Reading file from http
# Map it on class
# Find exact metrics