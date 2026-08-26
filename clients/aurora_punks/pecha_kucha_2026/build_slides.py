#!/usr/bin/env python3
"""
Build Aurora Punks Pecha Kucha Google Slides deck via Slides API.
Uses existing OAuth credentials from gdrive-upload.js pattern.
"""

import json
import time
import urllib.request
import urllib.parse
import urllib.error

CREDS_FILE = '/home/assistant/.claude/.gdrive-server-credentials.json'
KEYS_FILE = '/home/assistant/.claude/gcp-oauth.keys.json'
FOLDER_ID = '1hkJe4NrfJ3VrGZfgTjuiJANoK_yJlSkE'  # Aurora Punks / Pecha Kucha 2026

SLIDES_DATA = [
    {
        "title": "Cold open: the image of me",
        "visual": "VISUAL DIRECTION: John Blanche distorted figure crossed with Dali fantastic-escapist style. Dark, gothic, beautiful. No text, or just 'Robert / Aurora Punks' as a lower-third overlay.",
        "script": "Hi. I'm Robert. If you asked my brain to draw itself it would look like this. Distorted. Gothic. Escapist. There's beauty in the dark. That matters because everything I've built came from that place."
    },
    {
        "title": "The punk DIY origin",
        "visual": "VISUAL DIRECTION: Old hardcore scene photo. Basement show, zine cut-up, gig flyer, kid with a guitar. Grainy, raw. Shot on film if possible.",
        "script": "I came up in the hardcore scene. The rule there was simple. No label will sign you, you start one. No venue will book you, you put on the show. I never stopped applying that rule. It's the only rule I have."
    },
    {
        "title": "What drives me in 2026",
        "visual": "VISUAL DIRECTION: Two engines side-by-side. Or a phoenix half-formed. Comeback meets craft. Energy of two forces in tension.",
        "script": "Two engines drive me now. The comeback. Proving the model works after it broke. And the actual love of making things. Not the meetings about the things. The things. Those two engines together are what get me out of bed."
    },
    {
        "title": "How I lead, honest version",
        "visual": "VISUAL DIRECTION: Split image. Lighthouse on one side (steady, guiding), loose cannon on the other (volatile, energetic). Both real. Both mine.",
        "script": "Here's the honest version of how I lead. Likeable. Unfocused. Allergic to conflict. Sometimes a loose cannon. Never gives up. Glass always half full. Take the bundle. You don't get the good half without the rest. Hire me with eyes open."
    },
    {
        "title": "AP 2021, the origin in one beat",
        "visual": "VISUAL DIRECTION: Original Aurora Punks collective press shot or logo. Stockholm, 2021 energy. Optimistic, scrappy, collective.",
        "script": "Aurora Punks started in 2021 as a collective. Indie studios helping each other ship and sell games. Punk rock as a business model. That worked. And then it didn't. So we changed. Everything I'm going to say next is about that change."
    },
    {
        "title": "AP 2026, the line",
        "visual": "VISUAL DIRECTION: Full-bleed text on dark Blanche-style background. Text reads: A LOOSE BAND OF MERCENARIES. BATTLE SCARRED. LESS NAIVE. UNBREAKABLE.",
        "script": "Today AP is a loose band of mercenaries. Battle scarred. Less naive. Unbreakable. We dropped the collective scaffolding. We kept the punk part. The aesthetic is still ours. The business model is sharper now."
    },
    {
        "title": "No employees, on purpose",
        "visual": "VISUAL DIRECTION: Empty office at dusk, or a campfire with shadowed figures around it. Implied presence, no permanence. The space between missions.",
        "script": "We have no employees. Everyone in the band is a specialist who joins for a mission. When the mission ends they go back to other work. This is not a cost cut. It is the model. It's also one of the things I haven't fully figured out yet."
    },
    {
        "title": "The edge, said plain",
        "visual": "VISUAL DIRECTION: Full-bleed dark background with bold text: WE DON'T SELL HOURS. WE FIX THINGS. Clean, stark, declarative.",
        "script": "Most studios will sell you more hours. We won't. We sit with the problem until we understand it. Then we fix it. If we can't fix it we tell you. That's the offer. It's a smaller market than the hours business. It's the one we want."
    },
    {
        "title": "Proof, the work",
        "visual": "VISUAL DIRECTION: 3-up collage. The Finals key art / Ready or Not key art / a third placeholder for the Raw Fury co-dev title (keep vague, no title shown).",
        "script": "Two kinds of proof. AAA technical specialist work. Cross-platform commerce and console port release management on The Finals. Console porting and keyboard-to-controller UI adaptation on Ready or Not. And full-service co-dev for publishers on a Raw Fury title shipping 2026."
    },
    {
        "title": "What it feels like to work with us",
        "visual": "VISUAL DIRECTION: Fixer at a workbench, focused, calm. Or a hand on a shoulder in a crisis moment. Steady presence in a hard situation.",
        "script": "If you hire us it feels like calling in a fixer. We show up. We listen longer than you expect. We tell you what we actually think. Then we get the thing across the line and we leave. No upsell. No empire building."
    },
    {
        "title": "The dramatic pivot",
        "visual": "VISUAL DIRECTION: Demolition site, shed skin, or a Blanche-style ruined cathedral being repurposed. Something ending so something else can begin.",
        "script": "Here's what I won't dress up. We pivoted hard. Studios closed. The collective became a band. The team that built AP is not the team running it now. The pivot was the right call. It still hurt. I'm still metabolizing it."
    },
    {
        "title": "Hard question one",
        "visual": "VISUAL DIRECTION: Full-bleed text on Blanche-style dark background. Text: WHAT ARE WE? Bold, honest, unresolved.",
        "script": "Here's the question I'm sitting with in this room. What are we now. We know the work. We know the model. We're still finding the language for it. If you've been through a pivot this dramatic, I want to talk to you afterwards."
    },
    {
        "title": "Hard question two",
        "visual": "VISUAL DIRECTION: Full-bleed text on dark background: HOW DO YOU BUILD VALUE WITH NO EMPLOYEES? The tension of the model, stated plainly.",
        "script": "Second hard question. How do you build company value when no one is on payroll. Everyone in the band is freelance. The talent shows up for the mission and goes home. I have hypotheses. None proven yet. I want to be wrong about some of them."
    },
    {
        "title": "Hard question three",
        "visual": "VISUAL DIRECTION: A third attempt at building something. Scaffolding, half-built house, third match being struck. Not failure - iteration.",
        "script": "Third hard question. How do you start over when your first two attempts are public failures. Some of you have done this. I want to learn from you. Opinions I have plenty. Certainties not so much."
    },
    {
        "title": "The ask, part one: businesses",
        "visual": "VISUAL DIRECTION: A studio in trouble. Tangled cables, a roadmap with a hole in it, a fire to put out. The moment before someone calls in help.",
        "script": "Two specific asks from this room. First. We're looking for studios that need fixing. Stuck production. A publishing deal wobbling. A tech problem nobody can crack. Send them our way. We'll know within a call if we can help."
    },
    {
        "title": "The ask, part two: network",
        "visual": "VISUAL DIRECTION: Small circle of figures around a fire. Quiet conversation. Peer exchange, not networking performance.",
        "script": "Second ask. I want peers who've done dramatic pivots and survived. I want to compare notes. I want someone to tell me when I'm being a loose cannon. Network beats roadmap for me right now. Find me at the bar."
    },
    {
        "title": "What I bring back, the scars",
        "visual": "VISUAL DIRECTION: A scar, a broken object repaired with kintsugi gold, or a stark portrait. Beauty in what was broken. Experience as credential.",
        "script": "Here's what I bring in return. I've closed three studios through bankruptcy. I've laid off fifty developers. If you're anywhere near that territory I am useful to talk to. I know what the boring paperwork looks like. I know what the phone calls feel like."
    },
    {
        "title": "What I bring back, the playbook",
        "visual": "VISUAL DIRECTION: Hands writing in a notebook. Or a chess board mid-game. Deliberate, practiced, the result of hard-won pattern recognition.",
        "script": "I know how to navigate financial hardship without destroying your reputation or your relationships. There's a playbook for the hard parts. Most founders don't get exposed to it until they need it and it's already too late. I can shorten that learning curve."
    },
    {
        "title": "The line you leave with",
        "visual": "VISUAL DIRECTION: Full-bleed text on Blanche-Dali key visual background: DON'T WAIT TOO LONG BEFORE KILLING THE DARLING. The lesson, stated as command.",
        "script": "If you take one thing from these six minutes. Don't wait too long before killing the darling. The project. The hire. The strategy. The studio. Whatever it is. The cost of waiting is always worse than the cost of cutting. I waited too long three times. You don't have to."
    },
    {
        "title": "Close",
        "visual": "VISUAL DIRECTION: Final Blanche-Dali image. Lower-third text overlay: robert@aurorapunks.com and Aurora Punks wordmark. Warm, direct, open.",
        "script": "I'm Robert. Aurora Punks. Loose band of mercenaries. We fix things. Find me at the bar. I owe a lot of you a drink and a long conversation. Thank you."
    },
]


def load_token():
    with open(CREDS_FILE) as f:
        creds = json.load(f)
    with open(KEYS_FILE) as f:
        keys = json.load(f)['installed']

    # Refresh if expired or close to expiry
    if creds.get('expiry_date', 0) < (time.time() * 1000) + 60000:
        print("Refreshing token...")
        params = urllib.parse.urlencode({
            'client_id': keys['client_id'],
            'client_secret': keys['client_secret'],
            'refresh_token': creds['refresh_token'],
            'grant_type': 'refresh_token',
        }).encode()
        req = urllib.request.Request(
            'https://oauth2.googleapis.com/token',
            data=params, method='POST'
        )
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read())
        creds['access_token'] = data['access_token']
        creds['expiry_date'] = int(time.time() * 1000) + data['expires_in'] * 1000
        with open(CREDS_FILE, 'w') as f:
            json.dump(creds, f, indent=2)

    return creds['access_token']


def api(token, method, url, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
        },
        method=method
    )
    try:
        with urllib.request.urlopen(req) as resp:
            if resp.status == 204:
                return {}
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read()
        raise Exception(f"HTTP {e.code} {url}: {body[:500]}")


def create_presentation(token, title, folder_id):
    # Create via Drive API so we can set the parent folder
    result = api(token, 'POST',
        'https://www.googleapis.com/drive/v3/files?fields=id,name,webViewLink',
        {
            "name": title,
            "mimeType": "application/vnd.google-apps.presentation",
            "parents": [folder_id]
        }
    )
    return result['id'], result['webViewLink']


def get_presentation(token, pres_id):
    return api(token, 'GET', f'https://slides.googleapis.com/v1/presentations/{pres_id}')


def batch_update(token, pres_id, requests):
    return api(token, 'POST',
        f'https://slides.googleapis.com/v1/presentations/{pres_id}:batchUpdate',
        {"requests": requests}
    )


def pt(px):
    """Convert pixels to EMU (English Metric Units). 1pt = 12700 EMU. 1px ~ 0.75pt."""
    return int(px * 0.75 * 12700)


def emu(points):
    """Points to EMU."""
    return int(points * 12700)


def build_requests(pres, slides_data):
    """Build all batchUpdate requests for the presentation."""
    requests = []

    existing_slides = pres['slides']
    # We start with 1 slide. Add 19 more.
    slide_ids = [f'slide_{i+1}' for i in range(20)]

    # Step 1: Add slides 2-20
    for i in range(1, 20):
        requests.append({
            "createSlide": {
                "objectId": slide_ids[i],
                "insertionIndex": i,
                "slideLayoutReference": {"predefinedLayout": "BLANK"}
            }
        })

    # Fix slide 1 - delete existing content and set blank layout
    first_slide = existing_slides[0]
    first_slide_id = first_slide['objectId']
    slide_ids[0] = first_slide_id

    # Delete default placeholders on slide 1
    for elem in first_slide.get('pageElements', []):
        requests.append({"deleteObject": {"objectId": elem['objectId']}})

    return requests, slide_ids


def add_content_requests(slide_id, slide_data, slide_index):
    """Build requests to add title + visual + notes to a slide."""
    requests = []
    title_id = f'{slide_id}_title'
    body_id = f'{slide_id}_body'

    # Slide dimensions: 9144000 x 5143500 EMU (standard 16:9)
    W = 9144000
    H = 5143500

    # Title box: top strip, full width, ~12% height
    title_h = int(H * 0.12)
    requests.append({
        "createShape": {
            "objectId": title_id,
            "shapeType": "TEXT_BOX",
            "elementProperties": {
                "pageObjectId": slide_id,
                "size": {
                    "width": {"magnitude": W - emu(60), "unit": "EMU"},
                    "height": {"magnitude": title_h, "unit": "EMU"}
                },
                "transform": {
                    "scaleX": 1, "scaleY": 1,
                    "translateX": emu(30),
                    "translateY": emu(20),
                    "unit": "EMU"
                }
            }
        }
    })

    # Title text
    slide_num = slide_index + 1
    title_text = f"{slide_num}. {slide_data['title']}"
    requests.append({
        "insertText": {
            "objectId": title_id,
            "text": title_text,
            "insertionIndex": 0
        }
    })

    # Title formatting: bold, 24pt, white on dark background via shape background
    requests.append({
        "updateTextStyle": {
            "objectId": title_id,
            "style": {
                "fontSize": {"magnitude": 22, "unit": "PT"},
                "bold": True,
                "foregroundColor": {
                    "opaqueColor": {"rgbColor": {"red": 0.95, "green": 0.95, "blue": 0.95}}
                }
            },
            "textRange": {"type": "ALL"},
            "fields": "fontSize,bold,foregroundColor"
        }
    })

    # Title shape background: dark charcoal
    requests.append({
        "updateShapeProperties": {
            "objectId": title_id,
            "shapeProperties": {
                "shapeBackgroundFill": {
                    "solidFill": {
                        "color": {"rgbColor": {"red": 0.13, "green": 0.13, "blue": 0.15}}
                    }
                }
            },
            "fields": "shapeBackgroundFill"
        }
    })

    # Body text box: below title, nearly full slide
    body_top = title_h + emu(10)
    body_h = H - body_top - emu(20)
    requests.append({
        "createShape": {
            "objectId": body_id,
            "shapeType": "TEXT_BOX",
            "elementProperties": {
                "pageObjectId": slide_id,
                "size": {
                    "width": {"magnitude": W - emu(60), "unit": "EMU"},
                    "height": {"magnitude": body_h, "unit": "EMU"}
                },
                "transform": {
                    "scaleX": 1, "scaleY": 1,
                    "translateX": emu(30),
                    "translateY": body_top,
                    "unit": "EMU"
                }
            }
        }
    })

    # Body text
    requests.append({
        "insertText": {
            "objectId": body_id,
            "text": slide_data['visual'],
            "insertionIndex": 0
        }
    })

    # Body text formatting: italic, 16pt, light grey
    requests.append({
        "updateTextStyle": {
            "objectId": body_id,
            "style": {
                "fontSize": {"magnitude": 15, "unit": "PT"},
                "italic": True,
                "foregroundColor": {
                    "opaqueColor": {"rgbColor": {"red": 0.75, "green": 0.75, "blue": 0.78}}
                }
            },
            "textRange": {"type": "ALL"},
            "fields": "fontSize,italic,foregroundColor"
        }
    })

    # Body shape background: very dark, near-black
    requests.append({
        "updateShapeProperties": {
            "objectId": body_id,
            "shapeProperties": {
                "shapeBackgroundFill": {
                    "solidFill": {
                        "color": {"rgbColor": {"red": 0.08, "green": 0.08, "blue": 0.10}}
                    }
                }
            },
            "fields": "shapeBackgroundFill"
        }
    })

    return requests


def set_slide_background(slide_id, dark=True):
    """Set slide background to dark."""
    return [{
        "updatePageProperties": {
            "objectId": slide_id,
            "pageProperties": {
                "pageBackgroundFill": {
                    "solidFill": {
                        "color": {
                            "rgbColor": {
                                "red": 0.06,
                                "green": 0.06,
                                "blue": 0.08
                            }
                        }
                    }
                }
            },
            "fields": "pageBackgroundFill"
        }
    }]


def set_speaker_notes(token, pres_id, slide_id, notes_text):
    """Set speaker notes on a slide."""
    # Get the current slide to find notes page object ID
    pres = get_presentation(token, pres_id)
    for slide in pres['slides']:
        if slide['objectId'] == slide_id:
            notes_page = slide.get('slideProperties', {}).get('notesPage', {})
            notes_id = notes_page.get('notesProperties', {}).get('speakerNotesObjectId')
            if notes_id:
                return [{
                    "insertText": {
                        "objectId": notes_id,
                        "text": notes_text,
                        "insertionIndex": 0
                    }
                }]
    return []


def share_file(token, file_id, email, role='writer'):
    """Share file with an email address."""
    api(token, 'POST',
        f'https://www.googleapis.com/drive/v3/files/{file_id}/permissions?sendNotificationEmail=false',
        {"type": "user", "role": role, "emailAddress": email}
    )
    print(f"  Shared with {email} as {role}")


def publish_to_web(token, pres_id):
    """Publish presentation to the web for embedding/sharing."""
    # Use Drive API to publish
    result = api(token, 'POST',
        f'https://www.googleapis.com/drive/v3/files/{pres_id}/revisions/1?fields=id',
        {}
    )
    # Actually we use the Slides published URL pattern directly
    # The publish-to-web is done via the Drive API export or the webContentLink
    # For Google Slides, publish to web URL pattern is:
    # https://docs.google.com/presentation/d/{id}/pub?start=true&loop=false&delayms=20000
    return f"https://docs.google.com/presentation/d/{pres_id}/pub?start=true&loop=false&delayms=20000"


def main():
    print("Loading OAuth token...")
    token = load_token()

    print("Creating presentation in Drive...")
    pres_id, edit_url = create_presentation(
        token,
        "Aurora Punks - Pecha Kucha - Behold Summit 2026",
        FOLDER_ID
    )
    print(f"Created: {pres_id}")
    print(f"Edit URL: {edit_url}")

    print("Getting presentation structure...")
    pres = get_presentation(token, pres_id)

    print("Building initial slide structure...")
    structure_requests, slide_ids = build_requests(pres, SLIDES_DATA)

    print(f"Creating {len(structure_requests)} structural requests...")
    batch_update(token, pres_id, structure_requests)

    # Get fresh presentation to get actual slide IDs
    print("Getting updated presentation...")
    pres = get_presentation(token, pres_id)
    actual_slide_ids = [s['objectId'] for s in pres['slides']]
    print(f"Slides created: {len(actual_slide_ids)}")

    # Set backgrounds and add content to all slides
    all_content_requests = []

    for i, (slide_id, slide_data) in enumerate(zip(actual_slide_ids, SLIDES_DATA)):
        print(f"Building content for slide {i+1}: {slide_data['title']}")
        # Background
        all_content_requests.extend(set_slide_background(slide_id))
        # Content
        all_content_requests.extend(add_content_requests(slide_id, slide_data, i))

    print(f"Applying {len(all_content_requests)} content requests...")
    # Split into batches of 50 to avoid API limits
    batch_size = 50
    for i in range(0, len(all_content_requests), batch_size):
        batch = all_content_requests[i:i+batch_size]
        print(f"  Batch {i//batch_size + 1}/{(len(all_content_requests)+batch_size-1)//batch_size}...")
        batch_update(token, pres_id, batch)

    # Now add speaker notes - need fresh pres data for each slide's notes page ID
    print("Adding speaker notes...")
    pres = get_presentation(token, pres_id)

    notes_requests = []
    for slide, slide_data in zip(pres['slides'], SLIDES_DATA):
        slide_id = slide['objectId']
        notes_page = slide.get('slideProperties', {}).get('notesPage', {})
        notes_id = notes_page.get('notesProperties', {}).get('speakerNotesObjectId')
        if notes_id:
            notes_requests.append({
                "insertText": {
                    "objectId": notes_id,
                    "text": slide_data['script'],
                    "insertionIndex": 0
                }
            })
        else:
            print(f"  WARNING: No notes ID for slide {slide_id}")

    if notes_requests:
        print(f"Inserting {len(notes_requests)} speaker notes...")
        batch_update(token, pres_id, notes_requests)

    # Share with Robert's accounts
    print("Setting sharing permissions...")
    share_file(token, pres_id, 'robert@aurorapunks.com', 'writer')
    share_file(token, pres_id, 'johanrobert.backstrom@gmail.com', 'writer')

    # Construct publish URL
    publish_url = f"https://docs.google.com/presentation/d/{pres_id}/pub?start=true&loop=false&delayms=20000"

    print("\n" + "="*60)
    print("DONE")
    print("="*60)
    print(f"Edit URL:    {edit_url}")
    print(f"Publish URL: {publish_url}")
    print(f"Script:      /home/assistant/projects/clients/aurora_punks/pecha_kucha_2026/script.md")

    # Save results
    results = {
        "presentation_id": pres_id,
        "edit_url": edit_url,
        "publish_url": publish_url,
        "slide_count": len(actual_slide_ids),
        "script_path": "/home/assistant/projects/clients/aurora_punks/pecha_kucha_2026/script.md"
    }
    with open('/home/assistant/projects/clients/aurora_punks/pecha_kucha_2026/results.json', 'w') as f:
        json.dump(results, f, indent=2)
    print("\nResults saved to results.json")

    return results


if __name__ == '__main__':
    main()
