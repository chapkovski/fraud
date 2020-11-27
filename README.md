# Electoral fraud experiment

_Maggian, Chapkovski_

#### Group specification


- 7 people
- 2 roles - voter, candidate

#### Membership
- two membership subgroups  - red, blue
- 2 random voters are Red, 2 random voters are blue, one is randomly chosen to be blue or red
- 1 candidate is red, 1 candidate is blue
- voters don't keep membership across rounds
- candidates keep their memberships across rounds.
---
#### Payoff structure:
- Voters and candidates of party who got less votes get 0 in a round.
- Voters of a winning party gets X - C(v)
- A candidate of a winning party gets Y - C(f) |F (cost of fraud if fraud was committed).
- Ties are solved via coin tossing.
---
#### Fixed params (stable across treatments):
1. C(v) Cost of voting for voters
2. C(f) Cost of fraud for candidates
3. X - winning party' voter's payoff
4. Y - winning party' candidate's payoff
5. Number of rounds 

---
#### Treatments:
three treatments
* baseline
* fraud
* fraud + info

In fraud candidates can flip one opposite vote to their vote (if there are any votes for the opposite party)

In _fraud + info_  they can inform voters that the opposite candidate is going to commit a fraud after observing an opposite candidate decision. They can lie.

#### Game stages:

1. (All but baseline): Candidates take the decision on whether to commit a fraud. Voters wait
2. (Fraud + info): 

---
#### Code specification

- Ability to play 'single_player' game for the demo purposes plus for training purposes. In single_player the role of other 
6 players are performed by bots.
    - in single_playerthe role is not assigned randomly but based on `session.config` param `role`
    - to play it `single_player` `config.session` setting should be set to `true`
    - *TODO*: play `x` training rounds with single_player settings, plus one with real partners.
      
