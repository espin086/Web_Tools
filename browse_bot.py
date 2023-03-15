import webbrowser
import pyautogui, time
import argparse

def start_day():
    start_day = {"outlook_calendar": "https://ballard.amazon.com/owa/#path=/calendar/view/Week",
            "outlook_mail": "https://ballard.amazon.com/owa/#path=/mail",
            "trello": "https://trello.com/login",
            "google_calendar": "https://calendar.google.com/calendar/u/0/r?pli=1",
            "google_email": "https://mail.google.com/mail/u/0/?tab=cm#inbox",
            "slack": "https://slack.com/intl/en-in/get-started#/createnew",
            }

    for url in start_day:
        webbrowser.open(start_day[url])
    return None


def job_hunt():
    job_hunt = {"aws": "https://aws.amazon.com/",
            "resume": "https://drive.google.com/file/d/1OAlzeMl770155jhtHsLJOcBR3HhJwlFL/view?usp=share_link",
            "linkedin": "https://www.linkedin.com/jobs/",
            "indeed": "https://myjobs.indeed.com/saved",
            "trello": "https://trello.com/b/FwwUWzsq/job-search-2023",
            "podio": "https://podio.com/jj-espinoza/jobhunt",
            }

    for url in job_hunt:
        webbrowser.open(job_hunt[url])
    return None

def real_estate():
    real_estate = {"podio": "https://podio.com/jj-espinoza/jjc-capital",
            "airdna": "https://www.airdna.co/",
            "biggerpockets": "https://www.biggerpockets.com/",
            "propstream": "https://www.propstream.com/",
            "zillow": "https://www.zillow.com/"
            }
    for url in real_estate:
        webbrowser.open(real_estate[url])
    return None

def work_kpis():
    work_kpis = {"performance_tracker": "https://quip-amazon.com/To3HAV1OkHgf/Performance-Goal-Tracker-JJ-Espinoza#temp:C:EaSf5044d5f03a646bc8453dbd3c",
            "utilization": "https://proservecrm.lightning.force.com/lightning/r/Report/00O8b000007jLEoEAM/view",
            "open_roles": "https://proservecrm.lightning.force.com/lightning/r/Report/00O8b000007jXhkEAE/view",
            "eva": "https://proservecrm.lightning.force.com/lightning/r/Report/00O8b000007jLEyEAM/view",
            "timecard": "https://proservecrm.lightning.force.com/lightning/n/pse__Time_Entry",
            "accolades": "https://accolades.corp.amazon.com/",
            }

    for url in work_kpis:
        webbrowser.open(work_kpis[url])
    return None

def mymoney():
    mymoney = {"mint": "https://mint.intuit.com/",
            "bofa": "https://www.bankofamerica.com/",
            "chase": "https://www.chase.com/",
            "amex": "https://www.americanexpress.com/",
            "fidelity": "https://www.fidelity.com/",
            }
    for url in mymoney:
        webbrowser.open(mymoney[url])
    return None



def shutdown_rightbrowser():
    time.sleep(1)
    pyautogui.moveTo(1463, 54, duration=0.75)
    pyautogui.click(1307,91, duration=0.75)
    return None

def shutdown_centerbrowser():
    time.sleep(1)
    pyautogui.moveTo(264, 0, duration=0.75)
    pyautogui.click(25,38, duration=0.75)
    return None

def shutdown_leftbrowser():
    time.sleep(1)
    pyautogui.moveTo(-1619, 0, duration=0.75)
    pyautogui.click(-1906,41, duration=0.75)
    return None


def main(command):
    if command == "startwork":
        start_day()
    elif command == "endwork":
        shutdown_rightbrowser()
        shutdown_centerbrowser()
        shutdown_leftbrowser()
    elif command == "jobhunt":
        job_hunt()
    elif command == "realestate":
        real_estate()
    elif command == "mymoney":
        mymoney()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="manages browser during work")
    choices = ['startwork', 'workkpis', 'endwork', 'jobhunt', 'realestate', 'mymoney']
    parser.add_argument('command', metavar='command', type=str, help='type what you want to do: {0}'.format(choices), choices=choices)
    
    args = parser.parse_args()

    main(args.command)



