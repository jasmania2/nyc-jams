"""
generate_ics.py
Regenerates manhattan-jams.ics in the current directory.
Run locally or via GitHub Actions.
"""

import uuid
from datetime import date

OUTPUT_FILE = "manhattan-jams.ics"


def uid():
    return str(uuid.uuid4()) + "@manhattan-jams.nyc"


events = []


def ev(dtstart, dtend, summary, location, description, url="", rrule="FREQ=WEEKLY"):
    events.append({
        "uid": uid(),
        "dtstart": dtstart,
        "dtend": dtend,
        "summary": summary,
        "location": location,
        "description": description,
        "url": url,
        "rrule": rrule,
    })


# ── DAILY ──────────────────────────────────────────────────────────────────

ev("20260701T213000", "20260702T013000",
   "Don't Tell Mama — Nightly Audience Open Mic",
   "Don't Tell Mama, 343 W 46th St, Hell's Kitchen, NYC",
   "Write your name + song on a napkin and hand to pianist. Runs until 2:30am. "
   "No cover, 2-drink minimum. Live pianist from 5pm, singing waitstaff from 9pm.",
   "https://shows.donttellmamanyc.com/piano-bar",
   "FREQ=DAILY")

ev("20260701T140000", "20260701T180000",
   "Jazzcultural — Afternoon Jam in the Cafe",
   "Jazzcultural, 349 W 46th St, Midtown, NYC",
   "Rotating hosts daily — check smallslive.com for tonight's musician. Sit-in welcome.",
   "https://www.smallslive.com",
   "FREQ=DAILY")

ev("20260701T220000", "20260702T000000",
   "Jazzcultural — Late Night Jam in the Cafe",
   "Jazzcultural, 349 W 46th St, Midtown, NYC",
   "Rotating pianist hosts nightly 10pm-midnight. Check smallslive.com for host.",
   "https://www.smallslive.com",
   "FREQ=DAILY")

ev("20260701T234500", "20260702T040000",
   "Smalls Jazz Club — Late Night Jam Session",
   "Smalls Jazz Club, 183 W 10th St, West Village, NYC",
   "Nightly 11:45pm-4am with rotating hosts. Check smallslive.com for tonight's jam leader.",
   "https://www.smallslive.com",
   "FREQ=DAILY")

# ── SUNDAY ─────────────────────────────────────────────────────────────────

ev("20260705T200000", "20260705T220000",
   "Jazz By Jorei — Free Jazz Jam & Open Mic",
   "Sour Mouse, Lower East Side, NYC",
   "Free weekly Sunday jazz jam. Singers and musicians welcome to sign up or sit in.",
   "https://donyc.com/events/weekly/sun/free-jazz-jam-open-mic-every-sunday-tickets",
   "FREQ=WEEKLY;BYDAY=SU")

# ── MONDAY ─────────────────────────────────────────────────────────────────

ev("20260706T190000", "20260706T210000",
   "Big Ed's World Famous Blues Jam",
   "The Red Lion, 151 Bleecker St, Greenwich Village, NYC",
   "Weekly Monday blues jam hosted by Big Ed. $10 cover.",
   "",
   "FREQ=WEEKLY;BYDAY=MO")

ev("20260706T200000", "20260706T230000",
   "Five Spot Jazz — Monday Night Jam (FREE — No Music Charge)",
   "Five Spot Jazz, 231 E 9th St, East Village, NYC",
   "Doors 7:30pm. Rotating hosts: Allison Lee / Daniel Song (Juilliard-trained). "
   "Sit-in welcome. No music charge.",
   "https://www.fivespotjazz.com/upcomingshows",
   "FREQ=WEEKLY;BYDAY=MO")

ev("20260706T220000", "20260707T000000",
   "Richie Cannata's Monday Night Jam",
   "The Bitter End, 147 Bleecker St, Greenwich Village, NYC",
   "Hosted by Billy Joel's saxophonist. $12 cover.",
   "",
   "FREQ=WEEKLY;BYDAY=MO")

ev("20260706T213000", "20260707T000000",
   "Jim Caruso's Cast Party — Open Mic Variety Show",
   "Birdland, 315 W 44th St, Hell's Kitchen, NYC",
   "Legendary weekly open mic variety show since 1993. Bring your sheet music — "
   "sing with house band (Billy Stritch piano, Steve Doyle bass, Daniel Glass drums). "
   "Broadway stars and newcomers welcome. Cover + food/drink minimum.",
   "https://www.birdlandjazz.com/tm-event/jim-carusos-cast-party/",
   "FREQ=WEEKLY;BYDAY=MO")

ev("20260706T223000", "20260707T013000",
   "Smoke Jazz — Monday Night Jam (~10:30pm after headliners)",
   "Smoke Jazz & Supper Club, 2751 Broadway at 106th St, Upper West Side, NYC",
   "Jam begins after the 8:30pm headliner set (~10:30pm). "
   "Headliner shows at 6:30pm + 8:30pm. Cover + minimum. Call (212) 864-6662.",
   "https://smokejazz.com/",
   "FREQ=WEEKLY;BYDAY=MO")

ev("20260727T130000", "20260727T153000",
   "Jazz Foundation Monday Night Jam (Last Monday of month)",
   "Musicians Union, Midtown Manhattan, NYC",
   "Monthly jam — last Monday of each month. Free.",
   "https://jazzfoundation.org/monday-night-jam/",
   "FREQ=MONTHLY;BYDAY=-1MO")

# ── TUESDAY ────────────────────────────────────────────────────────────────

ev("20260707T130000", "20260707T180000",
   "Jazzcultural — Barry Harris Institute Free Lesson & Jam",
   "Jazzcultural, 349 W 46th St, Midtown, NYC",
   "Free admission. Recurring Tuesdays 1-6pm. Come learn, jam, sit in.",
   "https://www.smallslive.com",
   "FREQ=WEEKLY;BYDAY=TU")

ev("20260707T190000", "20260707T230000",
   "Melba's Tuesday Night Live Music Jam",
   "Melba's, 300 W 114th St, Harlem, NYC",
   "Live music jam with soul food, DJ, and dancing over dinner. "
   "Small venue — reservations strongly recommended. Call (212) 864-7777.",
   "https://www.melbasrestaurant.com/",
   "FREQ=WEEKLY;BYDAY=TU")

ev("20260707T210000", "20260707T230000",
   "Stonewall Inn Piano Bar — 2nd Floor (Tue)",
   "Stonewall Inn, 53 Christopher St, West Village, NYC",
   "Guest pianists + singing waitstaff & bartenders. No cover. Also Wednesdays 9pm.",
   "https://thestonewallinnnyc.com/weekly-events",
   "FREQ=WEEKLY;BYDAY=TU")

# ── WEDNESDAY ──────────────────────────────────────────────────────────────

ev("20260701T210000", "20260701T230000",
   "Stonewall Inn Piano Bar — 2nd Floor (Wed)",
   "Stonewall Inn, 53 Christopher St, West Village, NYC",
   "Guest pianists + singing waitstaff & bartenders. No cover. Also Tuesdays 9pm.",
   "https://thestonewallinnnyc.com/weekly-events",
   "FREQ=WEEKLY;BYDAY=WE")

# ── THURSDAY ───────────────────────────────────────────────────────────────

ev("20260702T170000", "20260702T210000",
   "Stonewall Inn — Eight Ball Lounge Karaoke",
   "Stonewall Inn, 53 Christopher St, West Village, NYC",
   "Hosted by Danielle. Pool table, drink specials, karaoke. 1st floor. No cover.",
   "https://thestonewallinnnyc.com/weekly-events",
   "FREQ=WEEKLY;BYDAY=TH")

ev("20260702T193000", "20260702T213000",
   "Thursday Open Mic — Music, Comedy, Poetry",
   "The Music Inn, 169 W 4th St, Greenwich Village, NYC",
   "All genres. Free. Line up early to sign up.",
   "",
   "FREQ=WEEKLY;BYDAY=TH")

ev("20260702T200000", "20260702T230000",
   "Ashford & Simpson's Sugar Bar — Open Mic",
   "Sugar Bar, 254 W 72nd St, Upper West Side, NYC",
   "$15 cover. Weekly Thursday open mic.",
   "",
   "FREQ=WEEKLY;BYDAY=TH")

# ── FRIDAY ─────────────────────────────────────────────────────────────────

ev("20260703T180000", "20260703T220000",
   "Stonewall Inn — Karaoke with Jazz & DJ Chauncey D",
   "Stonewall Inn, 53 Christopher St, West Village, NYC",
   "2nd floor. No cover. Weekly Friday.",
   "https://thestonewallinnnyc.com/weekly-events",
   "FREQ=WEEKLY;BYDAY=FR")

ev("20260703T223000", "20260704T010000",
   "One Flight Up — Friday Night Jam Session",
   "One Flight Up, 108 Greenwich St, Financial District, NYC",
   "Open Wed-Sat. Confirmed weekly Friday jam after headliner sets. "
   "$30 music room / $20 bar seating + 1 drink minimum.",
   "https://www.oneflightupjazz.com/",
   "FREQ=WEEKLY;BYDAY=FR")


# ── BUILD ICS ──────────────────────────────────────────────────────────────

def fold(line):
    """RFC 5545 line folding at 75 octets."""
    out = []
    while len(line.encode("utf-8")) > 75:
        out.append(line[:75])
        line = " " + line[75:]
    out.append(line)
    return "\r\n".join(out)


lines = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//Manhattan Jams Calendar//EN",
    "CALSCALE:GREGORIAN",
    "METHOD:PUBLISH",
    "X-WR-CALNAME:Manhattan Jam Sessions & Open Mics (NYC)",
    "X-WR-CALDESC:Recurring weekly jam sessions and open mics in Manhattan. "
    "Verified June 2026. Always call ahead — schedules change.",
    "X-WR-TIMEZONE:America/New_York",
    "BEGIN:VTIMEZONE",
    "TZID:America/New_York",
    "BEGIN:STANDARD",
    "DTSTART:19671029T020000",
    "RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10",
    "TZOFFSETFROM:-0400",
    "TZOFFSETTO:-0500",
    "TZNAME:EST",
    "END:STANDARD",
    "BEGIN:DAYLIGHT",
    "DTSTART:19870405T020000",
    "RRULE:FREQ=YEARLY;BYDAY=2SU;BYMONTH=3",
    "TZOFFSETFROM:-0500",
    "TZOFFSETTO:-0400",
    "TZNAME:EDT",
    "END:DAYLIGHT",
    "END:VTIMEZONE",
]

for e in events:
    desc = (e["description"]
            .replace("\\", "\\\\")
            .replace(";", "\\;")
            .replace(",", "\\,")
            .replace("\n", "\\n"))
    loc = (e["location"]
           .replace("\\", "\\\\")
           .replace(";", "\\;")
           .replace(",", "\\,"))
    s = (e["summary"]
         .replace("\\", "\\\\")
         .replace(";", "\\;")
         .replace(",", "\\,"))
    lines += [
        "BEGIN:VEVENT",
        "UID:" + e["uid"],
        "DTSTART;TZID=America/New_York:" + e["dtstart"],
        "DTEND;TZID=America/New_York:" + e["dtend"],
        "RRULE:" + e["rrule"],
        "SUMMARY:" + s,
        "LOCATION:" + loc,
        "DESCRIPTION:" + desc,
        "STATUS:CONFIRMED",
    ]
    if e["url"]:
        lines.append("URL:" + e["url"])
    lines.append("END:VEVENT")

lines.append("END:VCALENDAR")

output = "\r\n".join(fold(l) for l in lines) + "\r\n"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(output)

print(f"✓ Wrote {len(events)} events to {OUTPUT_FILE} (regenerated {date.today()})")
