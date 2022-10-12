This is a Data Structure and Algorithm Practice repo.

Efficient Teams

A coding competition is being organized on HackerRank Platform. The participants need to be grouped into teams where each team has exactly two candidates.
There are n candidates, where each candidate has a skill denoted bu skill[i]. A total of (n/2) teams are to be formed such that the total skill of each team if the same. The efficiency of a team is the same. The efficiency of a team is defined as the product of the skill levels of the two members i.e. for the skills [1,3], the efficiency of the team is 1 \* 3 = 3. Find the sum of efficiencies if all teams that can be formed satisfying the criteria. If there is no way to create teams that satisfy the condition return -1.

Note: It can be shown that the answer if always unique.

Example

The skills of the candidates are skill = [1,2,3,2].The can be paired as [[1,3], [2,2]]. The sum of skills for each team is the same i.e 4. The efficiency is computed as:

- Efficieny of [1,3]= 1 \* 3 = 3
- Efficiency of [2,2] = 2 \* 2 = 4

Return the sum of efficiencies, 3 + 4 = 7
