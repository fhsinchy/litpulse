from datetime import datetime

# Static holiday mapping (MM-DD format)
HOLIDAY_DATES = {
    "01-01": "New Year's Day",
    "02-14": "Valentine's Day",
    "03-08": "International Women's Day",
    "04-22": "Earth Day",
    "05-01": "Labour Day",
    "05-12": "Mother's Day",   # Update as needed
    "06-16": "Father's Day",   # Update as needed
    "07-04": "Independence Day (US)",
    "10-31": "Halloween",
    "11-28": "Thanksgiving",   # Update annually
    "12-24": "Christmas Eve",
    "12-25": "Christmas Day",
    "12-31": "New Year's Eve"
}

# Themes tied to specific holidays
HOLIDAY_TOPICS = {
    "Valentine's Day": "about love or romantic longing",
    "International Women's Day": "about women, strength or empowerment",
    "Mother's Day": "about mothers or family bonds",
    "Father's Day": "about fathers or guidance",
    "Independence Day": "about freedom or patriotism",
    "Christmas Day": "about peace, family, or giving",
    "Thanksgiving": "about gratitude or abundance",
    "New Year's Day": "about new beginnings or hope",
    "Halloween": "about fear, the supernatural, or mystery",
    "Earth Day": "about nature, the planet, or environmental care"
}

def get_theme_prompt(current_date=None):
    today = current_date or datetime.now()
    mm_dd = today.strftime("%m-%d")

    holiday_name = HOLIDAY_DATES.get(mm_dd)

    if holiday_name and holiday_name in HOLIDAY_TOPICS:
        return HOLIDAY_TOPICS[holiday_name], f"Holiday: {holiday_name}"

    return None, "No special theme"
