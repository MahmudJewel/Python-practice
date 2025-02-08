""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 15-06-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# st='m/l/xl     '
# lst = st.split('/')
# print(lst)

# from datetime import datetime
# start_date = "2024-08-19"
# start_date_parsed = datetime.strptime(start_date, "%Y-%m-%d")
# print(f"{start_date_parsed}")



from datetime import datetime, timedelta
import pytz
from typing import List, Dict, Any

def get_week_dates() -> Dict[str, str]:
    """Get the dates for each day of the current week."""
    today = datetime.now()
    current_day_index = today.weekday()  # 0 (Monday) to 6 (Sunday)
    
    # Adjust to make Sunday = 0 to match the original JavaScript logic
    current_day_index = (current_day_index + 1) % 7
    
    reference_dates = {}
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    
    for index, day in enumerate(days):
        date = today + timedelta(days=(index - current_day_index))
        reference_dates[day] = date.strftime('%Y-%m-%d')
    
    return reference_dates

def prepare_weekly_schedule_local_to_utc(weekly_schedule: List[Dict[str, Any]], timezone_str: str) -> List[Dict[str, Any]]:
    """
    Convert a weekly schedule from local timezone to UTC.
    
    Args:
        weekly_schedule: List of daily schedules with times in local timezone
        timezone_str: String representing the local timezone (e.g., 'America/New_York')
    
    Returns:
        List of daily schedules with times converted to UTC
    """
    # Initialize output structure
    output = {
        day: {
            'day': day.capitalize(),
            'is_open': False,
            'start_end_time': []
        }
        for day in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    }
    
    # Get reference dates for the current week
    reference_dates = get_week_dates()
    local_tz = pytz.timezone(timezone_str)
    utc_tz = pytz.UTC
    
    for day_obj in weekly_schedule:
        if not day_obj.get('start_end_time'):
            continue
            
        input_day_name = day_obj.get('day', '').lower()
        if not input_day_name or input_day_name not in reference_dates:
            continue
            
        ref_date = reference_dates[input_day_name]
        
        for slot in day_obj['start_end_time']:
            # Parse local times
            local_start_str = f"{ref_date} {slot['start_time']}"
            local_end_str = f"{ref_date} {slot['end_time']}"
            
            # Convert to datetime objects in local timezone
            local_start = datetime.strptime(local_start_str, '%Y-%m-%d %H:%M')
            local_start = local_tz.localize(local_start)
            
            local_end = datetime.strptime(local_end_str, '%Y-%m-%d %H:%M')
            local_end = local_tz.localize(local_end)
            
            # If end time is earlier than or equal to start time, add a day to end time
            if not local_end > local_start:
                local_end += timedelta(days=1)
            
            # Convert to UTC
            utc_start = local_start.astimezone(utc_tz)
            utc_end = local_end.astimezone(utc_tz)
            
            # Get UTC dates and days
            utc_start_date = utc_start.strftime('%Y-%m-%d')
            utc_end_date = utc_end.strftime('%Y-%m-%d')
            utc_start_day = utc_start.strftime('%A').lower()
            utc_end_day = utc_end.strftime('%A').lower()
            
            if utc_start_date == utc_end_date:
                # Entire slot falls on one UTC day
                output[utc_start_day]['start_end_time'].append({
                    'start_time': utc_start.strftime('%H:%M'),
                    'end_time': utc_end.strftime('%H:%M'),
                    'is_full_day': slot.get('is_full_day', False)
                })
            else:
                # Slot spans two UTC days - split it
                output[utc_start_day]['start_end_time'].append({
                    'start_time': utc_start.strftime('%H:%M'),
                    'end_time': '23:59',
                    'is_full_day': False
                })
                output[utc_end_day]['start_end_time'].append({
                    'start_time': '00:00',
                    'end_time': utc_end.strftime('%H:%M'),
                    'is_full_day': False
                })
    
    # Update is_open flags and prepare final result
    result = []
    for day in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
        day_data = output[day]
        day_data['is_open'] = len(day_data['start_end_time']) > 0
        result.append(day_data)
    
    return result

# Example usage:
if __name__ == "__main__":
    # Sample input schedule (times in local timezone)
    sample_schedule = [
        {
            "day": "Monday",
            "is_open": True,
            "start_end_time": [
                # {"start_time": "09:00", "end_time": "17:00", "is_full_day": False}
                {
			"start_time": "00:00",
			"end_time": "23:59",
			"is_full_day": False
		}
            ]
        }
    ]
    
    # Convert schedule from EST to UTC
    utc_schedule = prepare_weekly_schedule_local_to_utc(sample_schedule, "America/New_York")
    print("UTC Schedule:", utc_schedule)
