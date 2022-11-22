def vss_baseball_reverse_column_swaper(column:str):
    match column:
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
        case "Fielding - Triple Plays (TP)":
            return "F_TP"
        case "Fielding - Passed Balls (PB)":
            return "F_PB"
        case _:
            print('')