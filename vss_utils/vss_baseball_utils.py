
def vss_baseball_graph_stat_types():
    return [
        'Player Stats'#
        ,'Team Stats'#
        ,'Head-to-Head'#
        ,'Batting by Position'#
        ,'Batting by Runners'#
        ,'Batting by Platoon (L/R vs. L/R)'#
        ,'Pitching by Runners'#
        ,'Pitching by Platoon (L/R vs. L/R)'#
    ]

def vss_baseball_reverse_column_swaper(column:str):
    match column:
        case "B_PA":
            return "Batting - Plate Appearances (PA)"
        case "B_AB":
            return "Batting - At Bats (AB)"
        case "B_R":
            return "Batting - Runs Scored (R)"
        case "B_H":
            return "Batting - Hits (H)"
        case "B_TB":
            return "Batting - Total Bases (TB)"
        case "B_2B":
            return "Batting - Doubles (2B)"
        case "B_3B":
            return "Batting - Triples (3B)"
        case "B_HR":
            return "Batting - Home Runs (HR)"
        case "B_HR4":
            return "Batting - Grand Slam (HR4)"
        case "B_RBI":
            return "Batting - Runs Batted In (RBI)"
        case "B_GW":
            return "Batting - Game Winning Hits (GW)"
        case "B_BB":
            return "Batting - Walks (BB)"
        case "B_IBB":
            return "Batting - Intentional Walks (IBB)"
        case "B_SO":
            return "Batting - Strikeouts (SO)"
        case "B_GDP":
            return "Batting - Ground Into Double Play (GIDP)"
        case "B_HP":
            return "Batting - Hit By Pitch (HBP)"
        case "B_SH":
            return "Batting - Sac Hits (SH)"
        case "B_SF":
            return "Batting - Sac Flys (SF)"
        case "B_SB":
            return "Batting - Stolen Bases (SB)"
        case "B_CS":
            return "Batting - Caught Stealing (CS)"
        case "B_CI":
            return "Batting - Catcher Interference (CI)"
        case "B_LOB":
            return "Batting - Left on Base (LOB)"
        case "P_CG":
            return "Pitching - Complete Game (CG)"
        case "P_SHO":
            return "Pitching - Shutout (SHO)"
        case "P_CSHO":
            return "Pitching - Complete Gm. Shutout (CSHO)"
        case "P_GF":
            return "Pitching - Game(s) Finished (GF)"
        case "P_TBF":
            return "Pitching - Total Batters Faced (TBF)"
        case "B_PA":
            return ""
        case "B_PA":
            return ""
        
        case _:
            # This should not happen, but it will raise an 
            # error to prevent memory shenanagans.
            raise Exception("Not a supported column.")
        
def vss_baseball_team_stats_column_swaper(column:str):
    ## Batting Stats
    match column:
        case "Batting - Plate Appearances (PA)":
            return "B_PA"
        case "Batting - At Bats (AB)":
            return "B_AB"
        case "Batting - Runs Scored (R)":
            return "B_R"
        case "Batting - Hits (H)":
            return "B_H"
        case "Batting - Total Bases (TB)":
            return "B_TB"
        case "Batting - Doubles (2B)":
            return "B_2B"
        case "Batting - Triples (3B)":
            return "B_3B"
        case "Batting - Home Runs (HR)":
            return "B_HR"
        case "Batting - Grand Slam (HR4)":
            return "B_HR4"
        case "Batting - Runs Batted In (RBI)":
            return "B_RBI"
        case "Batting - Game Winning Hits (GW)":
            return "B_GW"
        case "Batting - Walks (BB)":
            return "B_BB"
        case "Batting - Intentional Walks (IBB)":
            return "B_BB"
        case "Batting - Strikeouts (SO)":
            return "B_SO"
        case "Batting - Ground Into Double Play (GIDP)":
            return "B_GDP"
        case "Batting - Hit By Pitch (HBP)":
            return "B_HP" # This stat (Hit By Pitch) has the acronym HBP, but in retrosheet, this stat is called "HP"
        case "Batting - Sac Hits (SH)":
            return "B_SH"
        case "Batting - Sac Flys (SF)":
            return "B_SF"
        case "Batting - Stolen Bases (SB)":
            return "B_SB"
        case "Batting - Caught Stealing (CS)":
            return "B_CS"
        case "Batting - Catcher Interference (CI)":
            return "B_CI"  # This stat (Catcher's Interference) has the acronym CI, but in retrosheet, this stat is called "XI"
        case "Batting - Left on Base (LOB)":
            return "B_LOB"

        ## Pitching Stats

        case "Pitching - Complete Game (CG)":
            return "P_CG"
        case "Pitching - Shutout (SHO)":
            return "P_SHO"
        case "Pitching - Complete Gm. Shutout (CSHO)":
            return "P_CSHO"
        case "Pitching - Game(s) Finished (GF)":
            return "P_GF"
        case "Pitching - Total Batters Faced (TBF)":
            return "P_TBF"
        case "Pitching - Pitching Outs (P_OUT)": # P_OUT =/= putout
            return "P_OUT"
        case "Pitching - At Bats faced (AB)":
            return "P_AB"
        case "Pitching - Runs allowed (R)":
            return "P_R"
        case "Pitching - Earned Runs allowed (ER)":
            return "P_ER"
        case "Pitching - Hits allowed (H)":
            return "P_H"
        case "Pitching - Total Bases allowed (TB)":
            return "P_TB"
        case "Pitching - Doubles allowed (2B)":
            return "P_2B"
        case "Pitching - Triples allowed (3B)":
            return "P_3B"
        case "Pitching - Home Runs allowed (HR)":
            return "P_HR"
        case "Pitching - HR4":
            return "P_HR4"
        case "Pitching - Walks issued (BB)":
            return "P_BB"
        case "Pitching - Intentional Walks issued (IBB)":
            return "P_IBB"
        case "Pitching - Strikeouts (SO)":
            return "P_SO"
        case "Pitching - GIDP situations forced (GIDP)":
            return "P_GDP"
        case "Pitching - HBP":
            return "P_HP" # This stat (Hit By Pitch) has the acronym HBP, but in retrosheet, this stat is called "HP"
        case "Pitching - Sac Hits forced (SH)":
            return "P_SH"
        case "Pitching - Sac Flys forced (SF)":
            return "P_SF"
        case "Pitching - Catcher Interference (CI)":
            return "P_XI" # This stat (Catcher's Interference) has the acronym CI, but in retrosheet, this stat is called "XI"
        case "Pitching - Wild Pitches (WP)":
            return "P_WP"
        case "Pitching - Balks (BK)":
            return "P_BK"
        case "Pitching - Inherited Runners (IR)":
            return "P_IR"
        case "Pitching - Inherited Runners Scored (IRS)":
            return "P_IRS"
        case "Pitching - Ground Outs forced (GO)":
            return "P_GO"
        case "Pitching - Fly Outs forced (FO)":
            return "P_AO"
        case "Pitching - Pitches":
            return "P_PITCH"
        case "Pitching - Strikes":
            return "P_STRIKE"

        ## Fielding
        case "Fielding - Outs":
            return "F_OUT"
        case "Fielding - Total Chances (TC)":
            return "F_TC"
        case "Fielding - Put Outs (PO)":
            return "F_PO"
        case "Fielding - Assists (A)":
            return "F_A"
        case "Fielding - Errors (E)":
            return "F_E"
        case "Fielding - Double Plays (DP)":
            return "F_DP"
        case "Fielding - Triple Plays (DP)":
            return "F_TP"
        case "Fielding - Passed Balls (PB)":
            return "F_PB"
        case _:
            # This should not happen, but it will raise an 
            # error to prevent memory shenanagans.
            raise Exception("Not a supported column.")


def vss_baseball_team_stats_col_list():
    return [
        "Batting - Plate Appearances (PA)",
        "Batting - At Bats (AB)",
        "Batting - Runs Scored (R)",
        "Batting - Hits (H)",
        "Batting - Total Bases (TB)",
        "Batting - Doubles (2B)",
        "Batting - Triples (3B)",
        "Batting - Home Runs (HR)",
        "Batting - Grand Slam (HR4)",
        "Batting - Runs Batted In (RBI)",
        "Batting - Game Winning Hits (GW)",
        "Batting - Walks (BB)",
        "Batting - Intentional Walks (IBB)",
        "Batting - Strikeouts (SO)",
        "Batting - GDP",
        "Batting - Hit By Pitch (HBP)",
        "Batting - Sac Hits (SH)",
        "Batting - Sac Flys (SF)",
        "Batting - Stolen Bases (SB)",
        "Batting - Caught Stealing (CS)",
        "Batting - Catcher Interference (CI)",
        "Batting - Left on Base (LOB)",
        "Pitching - Complete Game (CG)",
        "Pitching - Shutout (SHO)",
        "Pitching - Complete Gm. Shutout (CSHO)",
        "Pitching - Total Batters Faced (TBF)",
        "Pitching - Pitching Outs (P_OUT)",
        "Pitching - At Bats faced (AB)",
        "Pitching - Runs allowed (R)",
        "Pitching - Earned Runs allowed (ER)",
        "Pitching - Hits allowed (H)",
        "Pitching - Total Bases allowed (TB)",
        "Pitching - Doubles allowed (2B)",
        "Pitching - Triples allowed (3B)",
        "Pitching - Home Runs allowed (HR)",
        "Pitching - Grand Slams allowed (HR4)",
        "Pitching - Walks issued (BB)",
        "Pitching - Intentional Walks issued (IBB)",
        "Pitching - Strikeouts (SO)",
        "Pitching - GIDP situations forced (GIDP)",
        "Pitching - Sac Hits forced (SH)",
        "Pitching - Sac Flys forced (SF)",
        "Pitching - Catcher Interference (CI)",
        "Pitching - Wild Pitches (WP)",
        "Pitching - Balks (BK)",
        "Pitching - Inherited Runners (IR)",
        "Pitching - Inherited Runners Scored (IRS)",
        "Pitching - Ground Outs forced (GO)",
        "Pitching - Fly Outs forced (FO)",
        "Pitching - Pitches",
        "Pitching - Strikes",
        "Fielding - Outs",
        "Fielding - Total Chances (TC)",
        "Fielding - Put Outs (PO)",
        "Fielding - Assists (A)",
        "Fielding - Errors (E)",
        "Fielding - Double Plays (DP)",
        "Fielding - Triple Plays (DP)",
        "Fielding - Passed Balls (PB)"
    ]

def vss_baseball_player_stats_column_swaper(column:str):
    ## Batting Stats
    match column:
        case "Batting Positon - Slot":
            return "slot"
        case "Batting Positon - Sequence #":
            return "seq"
        case "Batting - Plate Appearances (PA)":
            return "B_PA"
        case "Batting - At Bats (AB)":
            return "B_AB"
        case "Batting - Runs Scored (R)":
            return "B_R"
        case "Batting - Hits (H)":
            return "B_H"
        case "Batting - Total Bases (TB)":
            return "B_TB"
        case "Batting - Doubles (2B)":
            return "B_2B"
        case "Batting - Triples (3B)":
            return "B_3B"
        case "Batting - Home Runs (HR)":
            return "B_HR"
        case "Batting - Grand Slam (HR4)":
            return "B_HR4"
        case "Batting - Runs Batted In (RBI)":
            return "B_RBI"
        case "Batting - Game Winning Hits (GW)":
            return "B_GW"
        case "Batting - Walks (BB)":
            return "B_BB"
        case "Batting - Intentional Walks (IBB)":
            return "B_BB"
        case "Batting - Strikeouts (SO)":
            return "B_SO"   
        case "Batting - Ground Into Double Play (GIDP)":
            return "B_GDP"
        case "Batting - Hit By Pitch (HBP)":
            return "B_HP" # This stat (Hit By Pitch) has the acronym HBP, but in retrosheet, this stat is called "HP"
        case "Batting - Sac Hits (SH)":
            return "B_SH"
        case "Batting - Sac Flys (SF)":
            return "B_SF"
        case "Batting - Stolen Bases (SB)":
            return "B_SB"
        case "Batting - Caught Stealing (CS)":
            return "B_CS"
        case "Batting - Catcher Interference (CI)":
            return "B_CI"  # This stat (Catcher's Interference) has the acronym CI, but in retrosheet, this stat is called "XI"
        case "Batting - Left on Base (LOB)":
            return "B_LOB"

        ## Pitching Stats

        case "Pitching - Complete Game (CG)":
            return "P_CG"
        case "Pitching - Shutout (SHO)":
            return "P_SHO"
        case "Pitching - Complete Gm. Shutout (CSHO)":
            return "P_CSHO"
        case "Pitching - Game(s) Finished (GF)":
            return "P_GF"
        case "Pitching - Total Batters Faced (TBF)":
            return "P_TBF"
        case "Pitching - Pitching Outs (P_OUT)": # P_OUT =/= putout
            return "P_OUT"
        case "Pitching - At Bats faced (AB)":
            return "P_AB"
        case "Pitching - Runs allowed (R)":
            return "P_R"
        case "Pitching - Earned Runs allowed (ER)":
            return "P_ER"
        case "Pitching - Hits allowed (H)":
            return "P_H"
        case "Pitching - Total Bases allowed (TB)":
            return "P_TB"
        case "Pitching - Doubles allowed (2B)":
            return "P_2B"
        case "Pitching - Triples allowed (3B)":
            return "P_3B"
        case "Pitching - Home Runs allowed (HR)":
            return "P_HR"
        case "Pitching - Grand Slams allowed (HR4)":
            return "P_HR4"
        case "Pitching - Walks issued (BB)":
            return "P_BB"
        case "Pitching - Intentional Walks issued (IBB)":
            return "P_IBB"
        case "Pitching - Strikeouts (SO)":
            return "P_SO"
        case "Pitching - GIDP situations forced (GIDP)":
            return "P_GDP"
        case "Pitching - HBP":
            return "P_HP" # This stat (Hit By Pitch) has the acronym HBP, but in retrosheet, this stat is called "HP"
        case "Pitching - Sac Hits forced (SH)":
            return "P_SH"
        case "Pitching - Sac Flys forced (SF)":
            return "P_SF"
        case "Pitching - Catcher Interference (CI)":
            return "P_XI" # This stat (Catcher's Interference) has the acronym CI, but in retrosheet, this stat is called "XI"
        case "Pitching - Wild Pitches (WP)":
            return "P_WP"
        case "Pitching - Balks (BK)":
            return "P_BK"
        case "Pitching - Inherited Runners (IR)":
            return "P_IR"
        case "Pitching - Inherited Runners Scored (IRS)":
            return "P_IRS"
        case "Pitching - Ground Outs forced (GO)":
            return "P_GO"
        case "Pitching - Fly Outs forced (FO)":
            return "P_AO"
        case "Pitching - Pitches":
            return "P_PITCH"
        case "Pitching - Strikes":
            return "P_STRIKE"

        ## Fielding
        # case "Fielding - Outs":
        #     return "F_OUT"
        # case "Fielding - Total Chances (TC)":
        #     return "F_TC"
        # case "Fielding - Put Outs (PO)":
        #     return "F_PO"
        # case "Fielding - Assists (A)":
        #     return "F_A"
        # case "Fielding - Errors (E)":
        #     return "F_E"
        # case "Fielding - Double Plays (DP)":
        #     return "F_DP"
        # case "Fielding - Triple Plays (DP)":
        #     return "F_TP"
        # case "Fielding - Passed Balls (PB)":
        #     return "F_PB"
        case _:
            # This should not happen, but it will raise an 
            # error to prevent memory shenanagans.
            raise Exception("Not a supported column.")




def vss_baseball_player_stats_col_list():
    return [
        "Batting Positon - Slot",
        "Batting Positon - Sequence #",
        "Batting - Plate Appearances (PA)",
        "Batting - At Bats (AB)",
        "Batting - Runs Scored (R)",
        "Batting - Hits (H)",
        "Batting - Total Bases (TB)",
        "Batting - Doubles (2B)",
        "Batting - Triples (3B)",
        "Batting - Home Runs (HR)",
        "Batting - Grand Slam (HR4)",
        "Batting - Runs Batted In (RBI)",
        "Batting - Game Winning Hits (GW)",
        "Batting - Walks (BB)",
        "Batting - Intentional Walks (IBB)",
        "Batting - Strikeouts (SO)",
        "Batting - Ground Into Double Play (GIDP)",
        "Batting - Hit By Pitch (HBP)",
        "Batting - Sac Hits (SH)",
        "Batting - Sac Flys (SF)",
        "Batting - Stolen Bases (SB)",
        "Batting - Caught Stealing (CS)",
        "Batting - Catcher Interference (CI)",
        "Batting - Left on Base (LOB)",
        "Pitching - Complete Game (CG)",
        "Pitching - Shutout (SHO)",
        "Pitching - Complete Gm. Shutout (CSHO)",
        "Pitching - Total Batters Faced (TBF)",
        "Pitching - Pitching Outs (P_OUT)",
        "Pitching - At Bats faced (AB)",
        "Pitching - Runs allowed (R)",
        "Pitching - Earned Runs allowed (ER)",
        "Pitching - Hits allowed (H)",
        "Pitching - Total Bases allowed (TB)",
        "Pitching - Doubles allowed (2B)",
        "Pitching - Triples allowed (3B)",
        "Pitching - Home Runs allowed (HR)",
        "Pitching - Grand Slams allowed (HR4)",
        "Pitching - Walks issued (BB)",
        "Pitching - Intentional Walks issued (IBB)",
        "Pitching - Strikeouts (SO)",
        "Pitching - GIDP situations forced (GIDP)",
        "Pitching - Sac Hits forced (SH)",
        "Pitching - Sac Flys forced (SF)",
        "Pitching - Catcher Interference (CI)",
        "Pitching - Wild Pitches (WP)",
        "Pitching - Balks (BK)",
        "Pitching - Inherited Runners (IR)",
        "Pitching - Inherited Runners Scored (IRS)",
        "Pitching - Ground Outs forced (GO)",
        "Pitching - Fly Outs forced (FO)",
        "Pitching - Pitches",
        "Pitching - Strikes"
    ]


def vss_baseball_head_to_head_column_swaper(column:str):
    match column:
        case "Batting - Plate Appearances (PA)":
            return "B_PA"
        case "Batting - At Bats (AB)":
            return "B_AB"
        case "Batting - Hits (H)":
            return "B_H"
        case "Batting - Doubles (2B)":
            return "B_2B"
        case "Batting - Triples (3B)":
            return "B_3B"
        case "Batting - Home Runs (HR)":
            return "B_HR"
        case "Batting - Grand Slam (HR4)":
            return "B_HR4"
        case "Batting - Runs Batted In (RBI)":
            return "B_RBI"
        case "Batting - Walks (BB)":
            return "B_BB"
        case "Batting - Intentional Walks (IBB)":
            return "B_IBB"
        case "Batting - Total Bases (TB)":
            return "B_TB"
        case "Batting - Strikeouts (SO)":
            return "B_SO"
        case "Batting - Ground Into Double Play (GIDP)":
            return "B_GDP"
        case "Batting - Hit By Pitch (HBP)":
            return "B_HP" # This stat (Hit By Pitch) has the acronym HBP, but in retrosheet, this stat is called "HP"
        case "Batting - Sac Hits (SH)":
            return "B_SH"
        case "Batting - Sac Flys (SF)":
            return "B_SF"
        case "Batting - Catcher Interference (CI)":
            return "B_XI" # This stat (Catcher's Interference) has the acronym CI, but in retrosheet, this stat is called "XI"

def vss_baseball_head_to_head_col_list():
    return [
        "Batting - Plate Appearances (PA)",
        "Batting - At Bats (AB)",
        "Batting - Hits (H)",
        "Batting - Doubles (2B)",
        "Batting - Triples (3B)",
        "Batting - Home Runs (HR)",
        "Batting - Grand Slam (HR4)",
        "Batting - Runs Batted In (RBI)",
        "Batting - Walks (BB)",
        "Batting - Intentional Walks (IBB)",
        "Batting - Total Bases (TB)",
        "Batting - Strikeouts (SO)",
        "Batting - Ground Into Double Play (GIDP)",
        "Batting - Hit By Pitch (HBP)",
        "Batting - Sac Hits (SH)",
        "Batting - Sac Flys (SF)",
        "Batting - Catcher Interference (CI)"
    ]

def vss_baseball_batting_by_position_column_swaper(column:str):
    match column:
        case "Batting - Player Position":
            return "BAT_FLD_CD"
        case "Batting - Plate Appearances (PA)":
            return "B_PA"
        case "Batting - At Bats (AB)":
            return "B_AB"
        case "Batting - Hits (H)":
            return "B_H"
        case "Batting - Doubles (2B)":
            return "B_2B"
        case "Batting - Triples (3B)":
            return "B_3B"
        case "Batting - Home Runs (HR)":
            return "B_HR"
        case "Batting - Grand Slam (HR4)":
            return "B_HR4"
        case "Batting - Runs Batted In (RBI)":
            return "B_RBI"
        case "Batting - Walks (BB)":
            return "B_BB"
        case "Batting - Intentional Walks (IBB)":
            return "B_IBB"
        case "Batting - Total Bases (TB)":
            return "B_TB"
        case "Batting - Strikeouts (SO)":
            return "B_SO"
        case "Batting - Ground Into Double Play (GIDP)":
            return "B_GDP"
        case "Batting - Hit By Pitch (HBP)":
            return "B_HP" # This stat (Hit By Pitch) has the acronym HBP, but in retrosheet, this stat is called "HP"
        case "Batting - Sac Hits (SH)":
            return "B_SH"
        case "Batting - Sac Flys (SF)":
            return "B_SF"
        case "Batting - Catcher Interference (CI)":
            return "B_XI" # This stat (Catcher's Interference) has the acronym CI, but in retrosheet, this stat is called "XI"


def vss_baseball_batting_by_position_col_list():
    return [
        "Batting - Player Position",
        "Batting - Plate Appearances (PA)",
        "Batting - At Bats (AB)",
        "Batting - Hits (H)",
        "Batting - Doubles (2B)",
        "Batting - Triples (3B)",
        "Batting - Home Runs (HR)",
        "Batting - Grand Slam (HR4)",
        "Batting - Runs Batted In (RBI)",
        "Batting - Walks (BB)",
        "Batting - Intentional Walks (IBB)",
        "Batting - Total Bases (TB)",
        "Batting - Strikeouts (SO)",
        "Batting - Ground Into Double Play (GIDP)",
        "Batting - Hit By Pitch (HBP)",
        "Batting - Sac Hits (SH)",
        "Batting - Sac Flys (SF)",
        "Batting - Catcher Interference (CI)"
    ]


def vss_baseball_batting_by_runners_column_swaper(column:str):
    match column:
        case "Batting - Runners on base situation":
            return "SITUATION"
        case "Batting - Plate Appearances (PA)":
            return "B_PA"
        case "Batting - At Bats (AB)":
            return "B_AB"
        case "Batting - Hits (H)":
            return "B_H"
        case "Batting - Doubles (2B)":
            return "B_2B"
        case "Batting - Triples (3B)":
            return "B_3B"
        case "Batting - Home Runs (HR)":
            return "B_HR"
        case "Batting - Grand Slam (HR4)":
            return "B_HR4"
        case "Batting - Runs Batted In (RBI)":
            return "B_RBI"
        case "Batting - Walks (BB)":
            return "B_BB"
        case "Batting - Intentional Walks (IBB)":
            return "B_IBB"
        case "Batting - Total Bases (TB)":
            return "B_TB"
        case "Batting - Strikeouts (SO)":
            return "B_SO"
        case "Batting - Ground Into Double Play (GIDP)":
            return "B_GDP"
        case "Batting - Hit By Pitch (HBP)":
            return "B_HP" # This stat (Hit By Pitch) has the acronym HBP, but in retrosheet, this stat is called "HP"
        case "Batting - Sac Hits (SH)":
            return "B_SH"
        case "Batting - Sac Flys (SF)":
            return "B_SF"
        case "Batting - Catcher Interference (CI)":
            return "B_XI" # This stat (Catcher's Interference) has the acronym CI, but in retrosheet, this stat is called "XI"


def vss_baseball_batting_by_runners_col_list():
    return [
        "Batting - Runners on base situation",
        "Batting - Plate Appearances (PA)",
        "Batting - At Bats (AB)",
        "Batting - Hits (H)",
        "Batting - Doubles (2B)",
        "Batting - Triples (3B)",
        "Batting - Home Runs (HR)",
        "Batting - Grand Slam (HR4)",
        "Batting - Runs Batted In (RBI)",
        "Batting - Walks (BB)",
        "Batting - Intentional Walks (IBB)",
        "Batting - Total Bases (TB)",
        "Batting - Strikeouts (SO)",
        "Batting - Ground Into Double Play (GIDP)",
        "Batting - Hit By Pitch (HBP)",
        "Batting - Sac Hits (SH)",
        "Batting - Sac Flys (SF)",
        "Batting - Catcher Interference (CI)"
    ]

def vss_baseball_batting_by_platoon_column_swaper(column:str):
    match column:
        case "Batter's batting hand":
            return "RESP_BAT_HAND_CD"
        case "Pitcher's pitching hand":
            return "RESP_PIT_HAND_CD"
        case "Batting - Plate Appearances (PA)":
            return "B_PA"
        case "Batting - At Bats (AB)":
            return "B_AB"
        case "Batting - Hits (H)":
            return "B_H"
        case "Batting - Doubles (2B)":
            return "B_2B"
        case "Batting - Triples (3B)":
            return "B_3B"
        case "Batting - Home Runs (HR)":
            return "B_HR"
        case "Batting - Grand Slam (HR4)":
            return "B_HR4"
        case "Batting - Runs Batted In (RBI)":
            return "B_RBI"
        case "Batting - Walks (BB)":
            return "B_BB"
        case "Batting - Intentional Walks (IBB)":
            return "B_IBB"
        case "Batting - Total Bases (TB)":
            return "B_TB"
        case "Batting - Strikeouts (SO)":
            return "B_SO"
        case "Batting - Ground Into Double Play (GIDP)":
            return "B_GDP"
        case "Batting - Hit By Pitch (HBP)":
            return "B_HP" # This stat (Hit By Pitch) has the acronym HBP, but in retrosheet, this stat is called "HP"
        case "Batting - Sac Hits (SH)":
            return "B_SH"
        case "Batting - Sac Flys (SF)":
            return "B_SF"
        case "Batting - Catcher Interference (CI)":
            return "B_XI" # This stat (Catcher's Interference) has the acronym CI, but in retrosheet, this stat is called "XI"

def vss_baseball_batting_by_platoon_col_list():
    return [
        "Batter's batting hand",
        "Pitcher's pitching hand",
        "Batting - Plate Appearances (PA)",
        "Batting - At Bats (AB)",
        "Batting - Hits (H)",
        "Batting - Doubles (2B)",
        "Batting - Triples (3B)",
        "Batting - Home Runs (HR)",
        "Batting - Grand Slam (HR4)",
        "Batting - Runs Batted In (RBI)",
        "Batting - Walks (BB)",
        "Batting - Intentional Walks (IBB)",
        "Batting - Total Bases (TB)",
        "Batting - Strikeouts (SO)",
        "Batting - Ground Into Double Play (GIDP)",
        "Batting - Hit By Pitch (HBP)",
        "Batting - Sac Hits (SH)",
        "Batting - Sac Flys (SF)",
        "Batting - Catcher Interference (CI)"
    ]

def vss_baseball_pitching_by_runners_column_swaper(column:str):
    match column:
        case "Pitching - Runners on base situation":
            return "SITUATION"
        case "Pitching - PA":
            return "B_PA"
        case "Pitching - PA":
            return "B_PA"
        case "Pitching - At Bats faced (AB)":
            return "B_AB"
        case "Pitching - Hits allowed (H)":
            return "B_H"
        case "Pitching - Doubles allowed (2B)":
            return "B_2B"
        case "Pitching - Triples allowed (3B)":
            return "B_3B"
        case "Pitching - Home Runs allowed (HR)":
            return "B_HR"
        case "Pitching - Grand Slams allowed (HR4)":
            return "B_HR4"
        case "Pitching - RBI":
            return "B_RBI"
        case "Pitching - Walks issued (BB)":
            return "B_BB"
        case "Pitching - Intentional Walks issued (IBB)":
            return "B_IBB"
        case "Pitching - Total Bases allowed (TB)":
            return "B_TB"
        case "Pitching - Strikeouts (SO)":
            return "B_SO"
        case "Pitching - GIDP situations forced (GIDP)":
            return "B_GDP"
        case "Pitching - HBP":
            return "B_HP" # This stat (Hit By Pitch) has the acronym HBP, but in retrosheet, this stat is called "HP"
        case "Pitching - Sac Hits forced (SH)":
            return "B_SH"
        case "Pitching - Sac Flys forced (SF)":
            return "B_SF"
        case "Pitching - Catcher Interference (CI)":
            return "B_XI" # This stat (Catcher's Interference) has the acronym CI, but in retrosheet, this stat is called "XI"



def vss_baseball_pitching_by_runners_col_list():
    return [
        "Pitching- Runners on base situation",
        "Pitching- PA",
        "Pitching- AB",
        "Pitching- H",
        "Pitching- 2B",
        "Pitching- 3B",
        "Pitching- HR",
        "Pitching- Grand Slam (HR4)",
        "Pitching- RBI",
        "Pitching- BB",
        "Pitching- IBB",
        "Pitching- TB",
        "Pitching- SO",
        "Pitching- GDP",
        "Pitching - HBP",
        "Pitching - Sac Hits forced (SH)",
        "Pitching - Sac Flys forced (SF)",
        "Pitching - Catcher Interference (CI)"
    ]

def vss_baseball_pitching_by_platoon_column_swaper(column:str):
    match column:
        case "Batter's Pitching hand":
            return "RESP_BAT_HAND_CD"
        case "Pitcher's pitching hand":
            return "RESP_PIT_HAND_CD"
        case "Pitching - PA":
            return "B_PA"
        case "Pitching - PA":
            return "B_PA"
        case "Pitching - At Bats faced (AB)":
            return "B_AB"
        case "Pitching - Hits allowed (H)":
            return "B_H"
        case "Pitching - Doubles allowed (2B)":
            return "B_2B"
        case "Pitching - Triples allowed (3B)":
            return "B_3B"
        case "Pitching - Home Runs allowed (HR)":
            return "B_HR"
        case "Pitching - Grand Slams allowed (HR4)":
            return "B_HR4"
        case "Pitching - RBI":
            return "B_RBI"
        case "Pitching - Walks issued (BB)":
            return "B_BB"
        case "Pitching - Intentional Walks issued (IBB)":
            return "B_IBB"
        case "Pitching - Total Bases allowed (TB)":
            return "B_TB"
        case "Pitching - Strikeouts (SO)":
            return "B_SO"
        case "Pitching - GIDP situations forced (GIDP)":
            return "B_GDP"
        case "Pitching - HBP":
            return "B_HP" # This stat (Hit By Pitch) has the acronym HBP, but in retrosheet, this stat is called "HP"
        case "Pitching - Sac Hits forced (SH)":
            return "B_SH"
        case "Pitching - Sac Flys forced (SF)":
            return "B_SF"
        case "Pitching - Catcher Interference (CI)":
            return "B_XI" # This stat (Catcher's Interference) has the acronym CI, but in retrosheet, this stat is called "XI"

def vss_baseball_pitching_by_platoon_col_list():
    return [
        "Batter's Batting hand",
        "Pitcher's pitching hand",
        "Pitching - PA",
        "Pitching - At Bats faced (AB)",
        "Pitching - Hits allowed (H)",
        "Pitching - Doubles allowed (2B)",
        "Pitching - Triples allowed (3B)",
        "Pitching - Home Runs allowed (HR)",
        "Pitching - Grand Slams allowed (HR4)",
        "Pitching - RBI",
        "Pitching - Walks issued (BB)",
        "Pitching - Intentional Walks issued (IBB)",
        "Pitching - Total Bases allowed (TB)",
        "Pitching - Strikeouts (SO)",
        "Pitching - GIDP situations forced (GIDP)",
        "Pitching - HBP",
        "Pitching - Sac Hits forced (SH)",
        "Pitching - Sac Flys forced (SF)",
        "Pitching - Catcher Interference (CI)"
    ]

