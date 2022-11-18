
def vss_baseball_graph_stat_types():
    return [
        'Player Stats'
        ,'Team Stats'
        ,'Head-to-Head'
        ,'Batting by Position'
        ,'Batting By Runners'
        ,'Batting by Platoon (L/R vs. L/R)'
        ,'Pitching by Position'
        ,'Pitching By Runners'
        ,'Pitching by Platoon (L/R vs. L/R)'
    ]

def vss_baseball_team_stats_column_swaper(column:str):
    ## Batting Stats
    match column:
        case "Batting - PA":
            return "B_PA"
        case "Batting - AB":
            return "B_AB"
        case "Batting - R":
            return "B_R"
        case "Batting - H":
            return "B_H"
        case "Batting - TB":
            return "B_TB"
        case "Batting - 2B":
            return "B_2B"
        case "Batting - 3B":
            return "B_3B"
        case "Batting - HR":
            return "B_HR"
        case "Batting - Grand Slam (HR4)":
            return "B_HR"
        case "Batting - RBI":
            return "B_RBI"
        case "Batting - GW":
            return "B_GW"
        case "Batting - BB":
            return "B_BB"
        case "Batting - IBB":
            return "B_BB"
        case "Batting - SO":
            return "B_SO"
        case "Batting - GDP":
            return "B_GDP"
        case "Batting - HBP":
            return "B_HP" # This stat (Hit By Pitch) has the acronym HBP, but in retrosheet, this stat is called "HP"
        case "Batting - SH":
            return "B_SH"
        case "Batting - SF":
            return "B_SF"
        case "Batting - SB":
            return "B_SB"
        case "Batting - CS":
            return "B_CS"
        case "Batting - CI":
            return "B_CI"  # This stat (Catcher's Interference) has the acronym CI, but in retrosheet, this stat is called "XI"
        case "Batting - LOB":
            return "B_LOB"

        ## Pitching Stats

        case "Pitching - CG":
            return "P_CG"
        case "Pitching - SHO":
            return "P_SHO"
        case "Pitching - CSHO":
            return "P_CSHO"
        case "Pitching - GF":
            return "P_GF"
        case "Pitching - TBF":
            return "P_GF"
        case "Pitching - P_OUT": # P_OUT =/= putout
            return "P_OUT"
        case "Pitching - AB":
            return "P_AB"
        case "Pitching - R":
            return "P_R"
        case "Pitching - ER":
            return "P_ER"
        case "Pitching - H":
            return "P_H"
        case "Pitching - TB":
            return "P_TB"
        case "Pitching - 2B":
            return "P_2B"
        case "Pitching - 3B":
            return "P_3B"
        case "Pitching - HR":
            return "P_HR"
        case "Pitching - HR4":
            return "P_HR4"
        case "Pitching - BB":
            return "P_BB"
        case "Pitching - IBB":
            return "P_IBB"
        case "Pitching - SO":
            return "P_SO"
        case "Pitching - GDP":
            return "P_GDP"
        case "Pitching - HBP":
            return "P_HP" # This stat (Hit By Pitch) has the acronym HBP, but in retrosheet, this stat is called "HP"
        case "Pitching - SH":
            return "P_SH"
        case "Pitching - SF":
            return "P_SF"
        case "Pitching - CI":
            return "P_XI" # This stat (Catcher's Interference) has the acronym CI, but in retrosheet, this stat is called "XI"
        case "Pitching - WP":
            return "P_WP"
        case "Pitching - BK":
            return "P_BK"
        case "Pitching - IR":
            return "P_IR"
        case "Pitching - IRS":
            return "P_IRS"
        case "Pitching - GO":
            return "P_GO"
        case "Pitching - FO (AO)":
            return "P_AO"
        case "Pitching - Pitches":
            return "P_PITCH"
        case "Pitching - Strikes":
            return "P_STRIKE"

        ## Fielding
        case "Fielding - Outs":
            return "F_OUT"
        case "Fielding - TC":
            return "F_TC"
        case "Fielding - PO":
            return "F_PO"
        case "Fielding - A":
            return "F_A"
        case "Fielding - E":
            return "F_E"
        case "Fielding - DP":
            return "F_DP"
        case "Fielding - TP":
            return "F_TP"
        case "Fielding - PB":
            return "F_PB"
        case _:
            # This should not happen, but it will raise an 
            # error to prevent memory shenanagans.
            raise Exception("Not a supported column.")


def vss_baseball_team_stats_col_list():
    return [
        "Batting - PA",
        "Batting - AB",
        "Batting - R",
        "Batting - R",
        "Batting - H",
        "Batting - TB",
        "Batting - 2B",
        "Batting - 3B",
        "Batting - HR",
        "Batting - Grand Slam (HR4)",
        "Batting - RBI",
        "Batting - GW",
        "Batting - BB",
        "Batting - IBB",
        "Batting - SO",
        "Batting - GDP",
        "Batting - HBP",
        "Batting - SH",
        "Batting - SF",
        "Batting - SB",
        "Batting - CS",
        "Batting - CI",
        "Batting - LOB",
        "Pitching - CG",
        "Pitching - SHO",
        "Pitching - CSHO",
        "Pitching - TBF",
        "Pitching - P_OUT",
        "Pitching - AB",
        "Pitching - R",
        "Pitching - ER",
        "Pitching - H",
        "Pitching - TB",
        "Pitching - 2B",
        "Pitching - 3B",
        "Pitching - HR",
        "Pitching - Grand Slam (HR4)",
        "Pitching - BB",
        "Pitching - IBB",
        "Pitching - SO",
        "Pitching - GDP",
        "Pitching - SH",
        "Pitching - SF",
        "Pitching - CI",
        "Pitching - WP",
        "Pitching - BK",
        "Pitching - IR",
        "Pitching - IRS",
        "Pitching - GO",
        "Pitching - FO (AO)",
        "Pitching - Pitches",
        "Pitching - Strikes",
        "Fielding - Outs",
        "Fielding - TC",
        "Fielding - PO",
        "Fielding - A",
        "Fielding - E",
        "Fielding - DP",
        "Fielding - TP",
        "Fielding - PB"
    ]

def vss_baseball_player_stats_column_swaper(column:str):
    ## Batting Stats
    match column:
        case "Batting Positon - Slot":
            return "slot"
        case "Batting Positon - Sequence #":
            return "seq"
        case "Batting - PA":
            return "B_PA"
        case "Batting - AB":
            return "B_AB"
        case "Batting - R":
            return "B_R"
        case "Batting - H":
            return "B_H"
        case "Batting - TB":
            return "B_TB"
        case "Batting - 2B":
            return "B_2B"
        case "Batting - 3B":
            return "B_3B"
        case "Batting - HR":
            return "B_HR"
        case "Batting - Grand Slam (HR4)":
            return "B_HR"
        case "Batting - RBI":
            return "B_RBI"
        case "Batting - GW":
            return "B_GW"
        case "Batting - BB":
            return "B_BB"
        case "Batting - IBB":
            return "B_BB"
        case "Batting - SO":
            return "B_SO"   
        case "Batting - GDP":
            return "B_GDP"
        case "Batting - HBP":
            return "B_HP" # This stat (Hit By Pitch) has the acronym HBP, but in retrosheet, this stat is called "HP"
        case "Batting - SH":
            return "B_SH"
        case "Batting - SF":
            return "B_SF"
        case "Batting - SB":
            return "B_SB"
        case "Batting - CS":
            return "B_CS"
        case "Batting - CI":
            return "B_CI"  # This stat (Catcher's Interference) has the acronym CI, but in retrosheet, this stat is called "XI"
        case "Batting - LOB":
            return "B_LOB"

        ## Pitching Stats

        case "Pitching - CG":
            return "P_CG"
        case "Pitching - SHO":
            return "P_SHO"
        case "Pitching - CSHO":
            return "P_CSHO"
        case "Pitching - GF":
            return "P_GF"
        case "Pitching - TBF":
            return "P_GF"
        case "Pitching - P_OUT": # P_OUT =/= putout
            return "P_OUT"
        case "Pitching - AB":
            return "P_AB"
        case "Pitching - R":
            return "P_R"
        case "Pitching - ER":
            return "P_ER"
        case "Pitching - H":
            return "P_H"
        case "Pitching - TB":
            return "P_TB"
        case "Pitching - 2B":
            return "P_2B"
        case "Pitching - 3B":
            return "P_3B"
        case "Pitching - HR":
            return "P_HR"
        case "Pitching - HR4":
            return "P_HR4"
        case "Pitching - BB":
            return "P_BB"
        case "Pitching - IBB":
            return "P_IBB"
        case "Pitching - SO":
            return "P_SO"
        case "Pitching - GDP":
            return "P_GDP"
        case "Pitching - HBP":
            return "P_HP" # This stat (Hit By Pitch) has the acronym HBP, but in retrosheet, this stat is called "HP"
        case "Pitching - SH":
            return "P_SH"
        case "Pitching - SF":
            return "P_SF"
        case "Pitching - CI":
            return "P_XI" # This stat (Catcher's Interference) has the acronym CI, but in retrosheet, this stat is called "XI"
        case "Pitching - WP":
            return "P_WP"
        case "Pitching - BK":
            return "P_BK"
        case "Pitching - IR":
            return "P_IR"
        case "Pitching - IRS":
            return "P_IRS"
        case "Pitching - GO":
            return "P_GO"
        case "Pitching - FO (AO)":
            return "P_AO"
        case "Pitching - Pitches":
            return "P_PITCH"
        case "Pitching - Strikes":
            return "P_STRIKE"

        ## Fielding
        # case "Fielding - Outs":
        #     return "F_OUT"
        # case "Fielding - TC":
        #     return "F_TC"
        # case "Fielding - PO":
        #     return "F_PO"
        # case "Fielding - A":
        #     return "F_A"
        # case "Fielding - E":
        #     return "F_E"
        # case "Fielding - DP":
        #     return "F_DP"
        # case "Fielding - TP":
        #     return "F_TP"
        # case "Fielding - PB":
        #     return "F_PB"
        case _:
            # This should not happen, but it will raise an 
            # error to prevent memory shenanagans.
            raise Exception("Not a supported column.")




def vss_baseball_player_stats_col_list():
    return [
        "Batting Positon - Slot",
        "Batting Positon - Sequence #",
        "Batting - PA",
        "Batting - AB",
        "Batting - R",
        "Batting - R",
        "Batting - H",
        "Batting - TB",
        "Batting - 2B",
        "Batting - 3B",
        "Batting - HR",
        "Batting - Grand Slam (HR4)",
        "Batting - RBI",
        "Batting - GW",
        "Batting - BB",
        "Batting - IBB",
        "Batting - SO",
        "Batting - GDP",
        "Batting - HBP",
        "Batting - SH",
        "Batting - SF",
        "Batting - SB",
        "Batting - CS",
        "Batting - CI",
        "Batting - LOB",
        "Pitching - CG",
        "Pitching - SHO",
        "Pitching - CSHO",
        "Pitching - TBF",
        "Pitching - P_OUT",
        "Pitching - AB",
        "Pitching - R",
        "Pitching - ER",
        "Pitching - H",
        "Pitching - TB",
        "Pitching - 2B",
        "Pitching - 3B",
        "Pitching - HR",
        "Pitching - Grand Slam (HR4)",
        "Pitching - BB",
        "Pitching - IBB",
        "Pitching - SO",
        "Pitching - GDP",
        "Pitching - SH",
        "Pitching - SF",
        "Pitching - CI",
        "Pitching - WP",
        "Pitching - BK",
        "Pitching - IR",
        "Pitching - IRS",
        "Pitching - GO",
        "Pitching - FO (AO)",
        "Pitching - Pitches",
        "Pitching - Strikes"
    ]


def vss_baseball_head_to_head_column_swaper(column:str):
    match column:
        case "Batting - PA":
            return "B_PA"
        case "Batting - AB":
            return "B_AB"
        case "Batting - H":
            return "B_H"
        case "Batting - 2B":
            return "B_2B"
        case "Batting - 3B":
            return "B_3B"
        case "Batting - HR":
            return "B_HR"
        case "Batting - Grand Slam (HR4)":
            return "B_HR4"
        case "Batting - RBI":
            return "B_RBI"
        case "Batting - BB":
            return "B_BB"
        case "Batting - IBB":
            return "B_IBB"
        case "Batting - TB":
            return "B_TB"
        case "Batting - SO":
            return "B_SO"
        case "Batting - GDP":
            return "B_GDP"
        case "Pitching - HBP":
            return "P_HP" # This stat (Hit By Pitch) has the acronym HBP, but in retrosheet, this stat is called "HP"
        case "Pitching - SH":
            return "P_SH"
        case "Pitching - SF":
            return "P_SF"
        case "Pitching - CI":
            return "P_XI" # This stat (Catcher's Interference) has the acronym CI, but in retrosheet, this stat is called "XI"

def vss_baseball_head_to_head_col_list():
    return [
        "Batting - PA",
        "Batting - AB",
        "Batting - H",
        "Batting - 2B",
        "Batting - 3B",
        "Batting - HR",
        "Batting - Grand Slam (HR4)",
        "Batting - RBI",
        "Batting - BB",
        "Batting - IBB",
        "Batting - TB",
        "Batting - SO",
        "Batting - GDP",
        "Pitching - HBP",
        "Pitching - SH",
        "Pitching - SF",
        "Pitching - CI"
    ]

def vss_baseball_batting_by_position_column_swaper(column:str):
    match column:
        case "Batting - Player Position":
            return "BAT_FLD_CD"
        case "Batting - PA":
            return "B_PA"
        case "Batting - PA":
            return "B_PA"
        case "Batting - AB":
            return "B_AB"
        case "Batting - H":
            return "B_H"
        case "Batting - 2B":
            return "B_2B"
        case "Batting - 3B":
            return "B_3B"
        case "Batting - HR":
            return "B_HR"
        case "Batting - Grand Slam (HR4)":
            return "B_HR4"
        case "Batting - RBI":
            return "B_RBI"
        case "Batting - BB":
            return "B_BB"
        case "Batting - IBB":
            return "B_IBB"
        case "Batting - TB":
            return "B_TB"
        case "Batting - SO":
            return "B_SO"
        case "Batting - GDP":
            return "B_GDP"
        case "Pitching - HBP":
            return "P_HP" # This stat (Hit By Pitch) has the acronym HBP, but in retrosheet, this stat is called "HP"
        case "Pitching - SH":
            return "P_SH"
        case "Pitching - SF":
            return "P_SF"
        case "Pitching - CI":
            return "P_XI" # This stat (Catcher's Interference) has the acronym CI, but in retrosheet, this stat is called "XI"


def vss_baseball_batting_by_position_col_list():
    return [
        "Batting - Player Position"
        "Batting - PA",
        "Batting - AB",
        "Batting - H",
        "Batting - 2B",
        "Batting - 3B",
        "Batting - HR",
        "Batting - Grand Slam (HR4)",
        "Batting - RBI",
        "Batting - BB",
        "Batting - IBB",
        "Batting - TB",
        "Batting - SO",
        "Batting - GDP",
        "Pitching - HBP",
        "Pitching - SH",
        "Pitching - SF",
        "Pitching - CI"
    ]