from crewai import Crew
from dotenv import load_dotenv

from trip_planner.agents import TripAgents
from trip_planner.tasks import TripTasks

load_dotenv()


class TripCrew:
    """여행 플래너 Crew"""

    def __init__(self, origin: str, cities: str, date_range: str, interests: str):
        self.cities = cities
        self.origin = origin
        self.interests = interests
        self.date_range = date_range

    def run(self):
        """Crew를 실행하고 여행 계획을 생성합니다"""
        agents = TripAgents()
        tasks = TripTasks()

        # 에이전트 생성
        city_selector_agent = agents.city_selection_agent()
        local_expert_agent = agents.local_expert()
        travel_concierge_agent = agents.travel_concierge()

        # 태스크 생성
        identify_task = tasks.identify_task(
            city_selector_agent,
            self.origin,
            self.cities,
            self.interests,
            self.date_range
        )
        gather_task = tasks.gather_task(
            local_expert_agent,
            self.origin,
            self.interests,
            self.date_range
        )
        plan_task = tasks.plan_task(
            travel_concierge_agent,
            self.origin,
            self.interests,
            self.date_range
        )

        # Crew 생성 및 실행
        crew = Crew(
            agents=[
                city_selector_agent,
                local_expert_agent,
                travel_concierge_agent
            ],
            tasks=[identify_task, gather_task, plan_task],
            verbose=True
        )

        result = crew.kickoff()
        return result
