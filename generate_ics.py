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
   "Rotating pianist hosts 10pm-midnight. Check smallslive.com for host. "
   "Not confirmed Thu/Fri/Sat — call ahead on those nights.",
   "https://www.smallslive.com",
   "FREQ=WEEKLY;BYDAY=SU,MO,TU,WE")

ev("20260701T234500", "20260702T040000",
   "Smalls Jazz Club — Late Night Jam Session",
   "Smalls Jazz Club, 183 W 10th St, West Village, NYC",
   "Nightly 11:45pm-4am with rotating hosts. Check smallslive.com for tonight's jam leader.",
   "https://www.smallslive.com",
   "FREQ=DAILY")

# ── SUNDAY ─────────────────────────────────────────────────────────────────

ev("20260705T180000", "20260705T220000",
   "American Legion Post 398 — Organ Jazz Jam",
   "American Legion Post 398, 248 W 132nd St, Harlem, NYC",
   "The Harlem Groove Band. Harlem's last organ jazz house. "
   "Free (donations welcome). Down a few steps to the ground floor. Sign the book when you arrive.",
   "https://www.harlemlatenightjazz.org/harlem-late-night-jazz-weekly-events",
   "FREQ=WEEKLY;BYDAY=SU")

ev("20260705T153000", "20260705T184500",
   "Jazz By Jorei — Free Jazz Jam & Open Mic",
   "Sour Mouse, Lower East Side, NYC",
   "Free weekly Sunday jazz jam, 3:30–6:45pm. Singers and musicians welcome to sign up or sit in.",
   "https://donyc.com/events/weekly/sun/free-jazz-jam-open-mic-every-sunday-tickets",
   "FREQ=WEEKLY;BYDAY=SU")

# ── MONDAY ─────────────────────────────────────────────────────────────────

ev("20260706T170000", "20260706T213000",
   "Arthur's Tavern — Grove Street Stompers (Sit-ins Welcome)",
   "Arthur's Tavern, 57 Grove St, West Village, NYC",
   "The Grove Street Stompers have held Monday nights since 1962. "
   "Dixieland + traditional jazz. Professional and amateur musicians welcome to sit in. "
   "No cover ever. $15 minimum per person per set. Multiple sets nightly.",
   "https://arthurstavern.nyc/events/",
   "FREQ=WEEKLY;BYDAY=MO")

ev("20260706T190000", "20260706T230000",
   "NAMA — Monday Night Live Music Jam (Music of the Diaspora)",
   "New Amsterdam Musical Association (NAMA), 107 W 130th St, Central Harlem, NYC",
   "One of Harlem's longest-running live music jams. Rotating bands playing Jazz, Blues, and Rumba. "
   "7pm–11pm. Bring your instrument or just your ears. "
   "Confirmed on namaharlem.org for 2026.",
   "https://www.namaharlem.org",
   "FREQ=WEEKLY;BYDAY=MO")

ev("20260706T190000", "20260706T220000",
   "Phil's House of Blues at Silvana",
   "Silvana, 300 W 116th St, Harlem, NYC",
   "Blues/jazz with Phil Young (drums/leader) + rotating A-list collaborators. $10 cover.",
   "https://jazzgeneration.org/calendar",
   "FREQ=WEEKLY;BYDAY=MO")

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

ev("20260706T200000", "20260706T230000",
   "Gin Mill Speakeasy Sessions",
   "The Gin Mill, 442 Amsterdam Ave (at 81st St), Upper West Side, NYC",
   "Free happy hour (well drinks + draft beer) 8-9pm in the underground speakeasy, "
   "then free live concert 9-11pm. Rotating artists. No cover.",
   "https://www.theginmillnyc.com/private-events-venue/speakeasy/",
   "FREQ=WEEKLY;BYDAY=MO")

ev("20260706T183000", "20260706T213000",
   "Joanne — Open Mic Night",
   "Joanne Trattoria, 70 W 68th St, Upper West Side, NYC",
   "Hosted by Noah Landry. Singers, musicians, comedians, poets, storytellers welcome. "
   "Dinner served throughout. All genres. Weekly Monday.",
   "https://joannenyc.com/events/",
   "FREQ=WEEKLY;BYDAY=MO")

ev("20260706T210000", "20260707T000000",
   "Mona's — Monday Night Bluegrass Jam",
   "Mona's, 224 Ave B, East Village, NYC",
   "Hosted by Rick Snell since 2011. Appalachian fiddle music, bluegrass, old-school country. "
   "All levels welcome to join in. No cover. 9pm-midnight.",
   "https://www.ricksnell.org/monasbluegrass",
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


ev("20260727T130000", "20260727T153000",
   "Jazz Foundation Monday Night Jam (Last Monday of month)",
   "Musicians Union, Midtown Manhattan, NYC",
   "Monthly jam — last Monday of each month. Free.",
   "https://jazzfoundation.org/monday-night-jam/",
   "FREQ=MONTHLY;BYDAY=-1MO")

# ── TUESDAY ────────────────────────────────────────────────────────────────

ev("20260714T190000", "20260714T210000",
   "Reverie Room — Open Mic Night (2nd Tuesday)",
   "Reverie Room, 163 W 72nd St (above bodega), Upper West Side, NYC",
   "2nd Tuesday of each month. Sign-ups 6:30pm, show 7pm. 15 slots, 5 min each. "
   "Music, comedy, poetry. Alcohol-free. $10 bodega minimum. "
   "Check @reverieroomnyc on Instagram for exact dates.",
   "https://www.reverieroomnyc.com/open-mic-night",
   "FREQ=MONTHLY;BYDAY=2TU")

ev("20260707T200000", "20260707T230000",
   "Bar Bayeux — Tuesday Jazz Jam Session",
   "Bar Bayeux, 1066 Nostrand Ave, Prospect Lefferts Gardens, Brooklyn, NYC",
   "Weekly Tuesday jazz jam, 8–11pm. Rotating house band. "
   "Singers and instrumentalists welcome to sit in. "
   "No cover. One drink minimum. Complimentary vegan food and brownies.",
   "https://www.barbayeux.com/jazz",
   "FREQ=WEEKLY;BYDAY=TU")

ev("20260707T210000", "20260708T010000",
   "Mona's Hot Four — Trad-Jazz Jam Session",
   "Mona's, 224 Ave B, East Village, NYC",
   "Weekly late-night traditional jazz jam hosted by Dennis Lichtman's Mona's Hot Four since 2007. "
   "9pm til late. No cover, tips for the band appreciated.",
   "https://www.dennislichtman.com/monas",
   "FREQ=WEEKLY;BYDAY=TU")

ev("20260707T193000", "20260707T220000",
   "JazzWahi Weekly Jazz Jam",
   "Kismat Indian Restaurant, 603 Ft. Washington Ave at W. 187 St, Washington Heights, NYC",
   "Running since February 2015 (609+ jams as of Feb 2026). Over 800 musicians have played. "
   "Free, no cover, no minimum. All levels welcome. Music starts when you arrive.",
   "https://www.jazzwahi.org/jazz-jam",
   "FREQ=WEEKLY;BYDAY=TU")

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

ev("20260701T160000", "20260701T171500",
   "JazzWahi Jazz in Bennett Park (Outdoor, April–October)",
   "Bennett Park, Ft. Washington Ave between W. 183–185 St, Washington Heights, NYC",
   "Free outdoor jazz jam. April 15 to October 28 only. Weather permitting. "
   "The highest natural point in Manhattan.",
   "https://www.jazzwahi.org/jazz-jam",
   "FREQ=WEEKLY;BYDAY=WE;UNTIL=20261028T235959Z")

ev("20260701T210000", "20260702T000000",
   "The Lions Den Jam at NAMA",
   "New Amsterdam Musical Association (NAMA), 107 W 130th St, Central Harlem, NYC",
   "Masters Jam in the Lion's Den hosted by Harlem Late Night Jazz. "
   "NYC's best Young Lions jamming with the masters. NAMA founded 1904 — nation's oldest org for Black musicians. "
   "9pm–midnight. Confirmed on namaharlem.org for July 2026.",
   "https://www.namaharlem.org",
   "FREQ=WEEKLY;BYDAY=WE;UNTIL=20261231T235959Z")

ev("20260701T190000", "20260701T230000",
   "Corner Lounge — Jazz Jam",
   "Corner Lounge Bistro, 32 E 130th St (btw 5th & Madison), Harlem, NYC",
   "Weekly jazz jam. Also Saturdays 7-11pm.",
   "https://www.harlemonestop.com/event/34689/harlem-harlem-harlem-jazz-night-jam-session",
   "FREQ=WEEKLY;BYDAY=WE")

ev("20260701T200000", "20260702T000000",
   "Gin Mill — Wednesday Night Jam Session (Peter Brainin)",
   "The Gin Mill, 442 Amsterdam Ave (at 81st St), Upper West Side, NYC",
   "Weekly Wednesday jazz jam session hosted by saxophonist Peter Brainin. 8pm start. "
   "All levels welcome to sit in.",
   "https://www.theginmillnyc.com/",
   "FREQ=WEEKLY;BYDAY=WE")

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

ev("20260730T213000", "20260730T233000",
   "Hit the Stage! — Open Mic Jam at Triad (TENTATIVE)",
   "Triad Theatre, 158 W 72nd St, Upper West Side, NYC",
   "TENTATIVE — verify date at fourhandscollective.org before going. "
   "Hosted by Matt Baker's jazz trio (piano/bass/drums). All styles welcome. "
   "Bring 3 copies of sheet music with chord symbols. $10 cash cover. Doors 9pm.",
   "https://fourhandscollective.org/events",
   "FREQ=MONTHLY;BYDAY=-1TH")

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

ev("20260717T224500", "20260718T013000",
   "Dizzy's Club — Vocal Jam (3rd Friday monthly)",
   "Dizzy's Club at Jazz at Lincoln Center, Frederick P. Rose Hall, Broadway at 60th St, Midtown, NYC",
   "Monthly vocal jam — spotlight for singers in a collaborative setting alongside instrumentalists. "
   "All levels welcome. 1 drink minimum. Cover waived for 9pm Dizzy's Club set attendees. "
   "Other Fridays have an open Jam Session (all instruments, also 10:45pm). "
   "Check jazz.org/dizzys/late-night-sessions-at-dizzys-club/ for this month's schedule.",
   "https://jazz.org/dizzys/late-night-sessions-at-dizzys-club/",
   "FREQ=MONTHLY;BYDAY=3FR")

ev("20260703T223000", "20260704T010000",
   "One Flight Up — Friday Night Jam Session",
   "One Flight Up, 108 Greenwich St, Financial District, NYC",
   "Open Wed-Sat. Confirmed weekly Friday jam after headliner sets. "
   "$30 music room / $20 bar seating + 1 drink minimum.",
   "https://www.oneflightupjazz.com/",
   "FREQ=WEEKLY;BYDAY=FR")

# ── CLOSE UP (Mon + Wed–Sun) ───────────────────────────────────────────────

ev("20260706T233000", "20260707T010000",
   "Close Up — Late Night Jam Session",
   "Close Up, 154 Orchard St, Lower East Side, NYC",
   "Headliner set at 10:30pm, open jam 11:30pm-1am (sometimes 2am). "
   "Artist-driven jazz club. Closed Tuesdays. Check calendar for tonight's host.",
   "https://www.closeupnyc.com",
   "FREQ=WEEKLY;BYDAY=SU,MO,WE,TH,FR,SA")

# ── SATURDAY ───────────────────────────────────────────────────────────────

ev("20260704T220000", "20260705T033000",
   "Bessie's Place — Live Performance & Open Jam",
   "Bessie's Place Clubhouse, 458 W 145th St (btw Amsterdam & Convent), Hamilton Heights, NYC",
   "Saturday Nite Performance followed by open late-night jam session. "
   "Hosted by Resident Music Director Noel Simone Wippler & Friends. "
   "$10 suggested. Verify address before going — also listed as 50 W 145th St on some listings. "
   "Check @bessiesplacenow on Instagram for updates.",
   "https://www.instagram.com/bessiesplacenow/",
   "FREQ=WEEKLY;BYDAY=SA")

ev("20260704T190000", "20260704T230000",
   "Corner Lounge — Jazz Jam",
   "Corner Lounge Bistro, 32 E 130th St (btw 5th & Madison), Harlem, NYC",
   "Weekly jazz jam. Also Wednesdays 7-11pm.",
   "https://www.harlemonestop.com/event/34689/harlem-harlem-harlem-jazz-night-jam-session",
   "FREQ=WEEKLY;BYDAY=SA")


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
