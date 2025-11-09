from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

MICROSERVICE_LINK = "https://appbox.qatar.cmu.edu/313-teams/team_name/"

# Mentor mapping for all teams
MENTOR_MAPPING = {
    "1": "Seckhen",
    "2": "Aadi",
    "3": "Steve",
    "4": "Seckhen",
    "5": "Aadi",
    "6": "Steve"
}

@app.get("/team_info/{team_id}")
def get_team_info(team_id: int):

    if team_id is None:
        raise HTTPException(status_code=404, detail="Missing team id")

    team_id_str = str(team_id)

    # Check if team_id exists in our mentor mapping
    if team_id_str not in MENTOR_MAPPING:
        raise HTTPException(status_code=404, detail="Invalid team id")

    response = requests.get(MICROSERVICE_LINK + team_id_str)
    # You can check out what the response body looks like in the terminal using the print statement
    data = response.json()
    print(data)

    team_name = data["team_name"]

    return {
        "team_id": team_id,
        "team_name": team_name,
        "mentor": MENTOR_MAPPING[team_id_str]
    }
