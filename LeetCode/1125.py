"""
$1125. Smallest Sufficient Team
"""

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skills_dict = dict()
        for i in range(len(req_skills)):
            skills_dict[req_skills[i]] = 1 << i
        
        people_skills = []
        for i, p in enumerate(people):
            v = 0
            for s in p:
                v = v | skills_dict[s]
            people_skills.append(v)
        
        dps = [None for _ in range(1<<len(req_skills))]
        dps[0] = []
        for skill_set in range(len(dps)):
            if dps[skill_set] == None:
                continue
            for i, p in enumerate(people_skills):
                val = skill_set | p
                if skill_set == val:
                    continue
                if dps[val] == None or len(dps[val]) > len(dps[skill_set]) + 1:
                    dps[val] = dps[skill_set] + [i]
        return dps[-1]


"""
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skills = collections.defaultdict(int)
        satisfied_count = 0
        min_people = float("inf")
        picks = []
        best_pick = []
        
        def dfs(p, count):
            nonlocal satisfied_count, min_people, picks, best_pick, picks
            # print(p, picks, best_pick, satisfied_count, min_people)
            if p >= len(people) or satisfied_count >= len(req_skills):
                return None
            person = people[p]
            picks.append(p)
            for skill in person:
                if skills[skill] == 0:
                    satisfied_count += 1
                skills[skill] += 1
            if satisfied_count >= len(req_skills):
                if count+1 < min_people:
                    min_people = count + 1
                    best_pick = picks.copy()
            dfs(p+1, count+1)
            picks.pop(-1)
            for skill in person:
                skills[skill] -= 1
                if skills[skill] == 0:
                    satisfied_count -= 1
            dfs(p+1, count)
        
        dfs(0, 0)
        return best_pick
"""