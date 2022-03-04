import datetime

date = datetime.datetime.now()

# There is 22 Ranks in th game so each Rank costs about 4.5 abstract points

# Naming Ranks

allranks = ['I 1', 'i 1', 'I1', 'i1', 'Ir 1', 'ir 1', 'IR 1', 'Ir1', 'ir1', 'IR1', 'In 1', 'in 1', 'IN 1', 'In1', 'in1', 'IN1', 'Irn 1', 'irn 1', 'IRN 1', 'Irn1', 'irn1', 'IRN1', 'Iron 1', 'iron 1', 'IRON 1', 'Iron1', 'iron1', 'IRON1',
'I 2', 'i 2', 'I2', 'i2', 'Ir 2', 'ir 2', 'IR 2', 'Ir2', 'ir2', 'IR2', 'In 2', 'in 2', 'IN 2', 'In2', 'in2', 'IN2', 'Irn 2', 'irn 2', 'IRN 2', 'Irn2', 'irn2', 'IRN2', 'Iron 2', 'iron 2', 'IRON 2', 'Iron2', 'iron2', 'IRON2',
'I 3', 'i 3', 'I3', 'i3', 'Ir 3', 'ir 3', 'IR 3', 'Ir3', 'ir3', 'IR3', 'In 3', 'in 3', 'IN 3', 'In3', 'in3', 'IN3', 'Irn 3', 'irn 3', 'IRN 3', 'Irn3', 'irn3', 'IRN3', 'Iron 3', 'iron 3', 'IRON 3', 'Iron3', 'iron3', 'IRON3',
'B 1', 'b 1', 'B1', 'b1', 'Br 1', 'br 1', 'BR 1', 'Br1', 'br1', 'BR1', 'Bz 1', 'bz 1', 'BZ 1', 'Bz1', 'bz1', 'BZ1', 'Brz 1', 'brz 1', 'BRZ 1', 'Brz1', 'brz1', 'BRZ1', 'Bronze 1', 'bronze 1', 'BRONZE 1', 'Bronze1', 'bronze1', 'BRONZE1',
'B 2', 'b 2', 'B2', 'b2', 'Br 2', 'br 2', 'BR 2', 'Br2', 'br2', 'BR2', 'Bz 2', 'bz 2', 'BZ 2', 'Bz2', 'bz2', 'BZ2', 'Brz 2', 'brz 2', 'BRZ 2', 'Brz2', 'brz2', 'BRZ2', 'Bronze 2', 'bronze 2', 'BRONZE 2', 'Bronze2', 'bronze2', 'BRONZE2',
'B 3', 'b 3', 'B3', 'b3', 'Br 3', 'br 3', 'BR 3', 'Br3', 'br3', 'BR3', 'Bz 3', 'bz 3', 'BZ 3', 'Bz3', 'bz3', 'BZ3', 'Brz 3', 'brz 3', 'BRZ 3', 'Brz3', 'brz3', 'BRZ3', 'Bronze 3', 'bronze 3', 'BRONZE 3', 'Bronze3', 'bronze3', 'BRONZE3',
'S 1', 's 1', 'S1', 's1', 'Sl 1', 'sl 1', 'SL 1', 'Sl1', 'sl1', 'SL1', 'Sv 1', 'sv 1', 'SV 1', 'Sv1', 'sv1', 'SV1', 'Slv 1', 'slv 1', 'SLV 1', 'Slv1', 'slv1', 'SLV1', 'Silver 1', 'silver 1', 'SILVER 1', 'Silver1', 'silver1', 'SILVER1',
'S 2', 's 2', 'S2', 's2', 'Sl 2', 'sl 2', 'SL 2', 'Sl2', 'sl2', 'SL2', 'Sv 2', 'sv 2', 'SV 2', 'Sv2', 'sv2', 'SV2', 'Slv 2', 'slv 2', 'SLV 2', 'Slv2', 'slv2', 'SLV2', 'Silver 2', 'silver 2', 'SILVER 2', 'Silver2', 'silver2', 'SILVER2',
'S 3', 's 3', 'S3', 's3', 'Sl 3', 'sl 3', 'SL 3', 'Sl3', 'sl3', 'SL3', 'Sv 3', 'sv 3', 'SV 3', 'Sv3', 'sv3', 'SV3', 'Slv 3', 'slv 3', 'SLV 3', 'Slv3', 'slv3', 'SLV3', 'Silver 3', 'silver 3', 'SILVER 3', 'Silver3', 'silver3', 'SILVER3',
'G 1', 'g 1', 'G1', 'g1', 'Gl 1', 'gl 1', 'GL 1', 'Gl1', 'gl1', 'GL1', 'Gd 1', 'gd 1', 'GD 1', 'Gd1', 'gd1', 'GD1', 'Gld 1', 'gld 1', 'GLD 1', 'Gld1', 'gld1', 'GLD1', 'Gold 1', 'gold 1', 'GOLD 1', 'Gold1', 'gold1', 'GOLD1',
'G 2', 'g 2', 'G2', 'g2', 'Gl 2', 'gl 2', 'GL 2', 'Gl2', 'gl2', 'GL2', 'Gd 2', 'gd 2', 'GD 2', 'Gd2', 'gd2', 'GD2', 'Gld 2', 'gld 2', 'GLD 2', 'Gld2', 'gld2', 'GLD2', 'Gold 2', 'gold 2', 'GOLD 2', 'Gold2', 'gold2', 'GOLD2',
'G 3', 'g 3', 'G3', 'g3', 'Gl 3', 'gl 3', 'GL 3', 'Gl3', 'gl3', 'GL3', 'Gd 3', 'gd 3', 'GD 3', 'Gd3', 'gd3', 'GD3', 'Gld 3', 'gld 3', 'GLD 3', 'Gld3', 'gld3', 'GLD3', 'Gold 3', 'gold 3', 'GOLD 3', 'Gold3', 'gold3', 'GOLD3',
'P 1', 'p 1', 'P1', 'p1', 'Pl 1', 'pl 1', 'PL 1', 'Pl1', 'pl1', 'PL1', 'Pt 1', 'pt 1', 'PT 1', 'Pt1', 'pt1', 'PT1', 'Plt 1', 'plt 1', 'PLT 1', 'Plt1', 'plt1', 'PLT1', 'Platinum 1', 'platinum 1', 'PLATINUM 1', 'Platinum1', 'platinum1', 'PLATINUM1',
'P 2', 'p 2', 'P2', 'p2', 'Pl 2', 'pl 2', 'PL 2', 'Pl2', 'pl2', 'PL2', 'Pt 2', 'pt 2', 'PT 2', 'Pt2', 'pt2', 'PT2', 'Plt 2', 'plt 2', 'PLT 2', 'Plt2', 'plt2', 'PLT2', 'Platinum 2', 'platinum 2', 'PLATINUM 2', 'Platinum2', 'platinum2', 'PLATINUM2',
'P 3', 'p 3', 'P3', 'p3', 'Pl 3', 'pl 3', 'PL 3', 'Pl3', 'pl3', 'PL3', 'Pt 3', 'pt 3', 'PT 3', 'Pt3', 'pt3', 'PT3', 'Plt 3', 'plt 3', 'PLT 3', 'Plt3', 'plt3', 'PLT3', 'Platinum 3', 'platinum 3', 'PLATINUM 3', 'Platinum3', 'platinum3', 'PLATINUM3',
'D 1', 'd 1', 'D1', 'd1', 'Di 1', 'di 1', 'DI 1', 'Di1', 'di1', 'DI1', 'Dm 1', 'dm 1', 'DM 1', 'Dm1', 'dm1', 'DM1', 'Dmd 1', 'dmd 1', 'DMD 1', 'Dmd1', 'dmd1', 'DMD1', 'Diamond 1', 'diamond 1', 'DIAMOND 1', 'Diamond1', 'diamond1', 'DIAMOND1',
'D 2', 'd 2', 'D2', 'd2', 'Di 2', 'di 2', 'DI 2', 'Di2', 'di2', 'DI2', 'Dm 2', 'dm 2', 'DM 2', 'Dm2', 'dm2', 'DM2', 'Dmd 2', 'dmd 2', 'DMD 2', 'Dmd2', 'dmd2', 'DMD2', 'Diamond 2', 'diamond 2', 'DIAMOND 2', 'Diamond2', 'diamond2', 'DIAMOND2',
'D 3', 'd 3', 'D3', 'd3', 'Di 3', 'di 3', 'DI 3', 'Di3', 'di3', 'DI3', 'Dm 3', 'dm 3', 'DM 3', 'Dm3', 'dm3', 'DM3', 'Dmd 3', 'dmd 3', 'DMD 3', 'Dmd3', 'dmd3', 'DMD3', 'Diamond 3', 'diamond 3', 'DIAMOND 3', 'Diamond3', 'diamond3', 'DIAMOND3',
'Im 1', 'im 1', 'IM 1', 'Im1', 'im1', 'IM1', 'Il 1', 'il 1', 'IL 1', 'Il1', 'il1', 'IL1', 'Imm 1', 'imm 1', 'IMM 1', 'Imm1', 'imm1', 'IMM1', 'Immortal 1', 'immortal 1', 'IMMORTAL 1', 'Immortal1', 'immortal1', 'IMMORTAL1',
'Im 2', 'im 2', 'IM 2', 'Im2', 'im2', 'IM2', 'Il 2', 'il 2', 'IL 2', 'Il2', 'il2', 'IL2', 'Imm 2', 'imm 2', 'IMM 2', 'Imm2', 'imm2', 'IMM2', 'Immortal 2', 'immortal 2', 'IMMORTAL 2', 'Immortal2', 'immortal2', 'IMMORTAL2',
'Im 3', 'im 3', 'IM 3', 'Im3', 'im3', 'IM3', 'Il 3', 'il 3', 'IL 3', 'Il3', 'il3', 'IL3', 'Imm 3', 'imm 3', 'IMM 3', 'Imm3', 'imm3', 'IMM3', 'Immortal 3', 'immortal 3', 'IMMORTAL 3', 'Immortal3', 'immortal3', 'IMMORTAL3',
'R', 'r', 'Rd', 'rd', 'RD', 'Rt', 'rt', 'RT', 'Rad', 'rad', 'RAD', 'Rdt', 'rdt', 'RDT', 'Rnt', 'rnt', 'RNT', 'Radiant', 'radiant', 'RADIANT']

rank1 = ['I 1', 'i 1', 'I1', 'i1', 'Ir 1', 'ir 1', 'IR 1', 'Ir1', 'ir1', 'IR1', 'In 1', 'in 1', 'IN 1', 'In1', 'in1', 'IN1', 'Irn 1', 'irn 1', 'IRN 1', 'Irn1', 'irn1', 'IRN1', 'Iron 1', 'iron 1', 'IRON 1', 'Iron1', 'iron1', 'IRON1']
rank2 = ['I 2', 'i 2', 'I2', 'i2', 'Ir 2', 'ir 2', 'IR 2', 'Ir2', 'ir2', 'IR2', 'In 2', 'in 2', 'IN 2', 'In2', 'in2', 'IN2', 'Irn 2', 'irn 2', 'IRN 2', 'Irn2', 'irn2', 'IRN2', 'Iron 2', 'iron 2', 'IRON 2', 'Iron2', 'iron2', 'IRON2']
rank3 = ['I 3', 'i 3', 'I3', 'i3', 'Ir 3', 'ir 3', 'IR 3', 'Ir3', 'ir3', 'IR3', 'In 3', 'in 3', 'IN 3', 'In3', 'in3', 'IN3', 'Irn 3', 'irn 3', 'IRN 3', 'Irn3', 'irn3', 'IRN3', 'Iron 3', 'iron 3', 'IRON 3', 'Iron3', 'iron3', 'IRON3']
rank4 = ['B 1', 'b 1', 'B1', 'b1', 'Br 1', 'br 1', 'BR 1', 'Br1', 'br1', 'BR1', 'Bz 1', 'bz 1', 'BZ 1', 'Bz1', 'bz1', 'BZ1', 'Brz 1', 'brz 1', 'BRZ 1', 'Brz1', 'brz1', 'BRZ1', 'Bronze 1', 'bronze 1', 'BRONZE 1', 'Bronze1', 'bronze1', 'BRONZE1']
rank5 = ['B 2', 'b 2', 'B2', 'b2', 'Br 2', 'br 2', 'BR 2', 'Br2', 'br2', 'BR2', 'Bz 2', 'bz 2', 'BZ 2', 'Bz2', 'bz2', 'BZ2', 'Brz 2', 'brz 2', 'BRZ 2', 'Brz2', 'brz2', 'BRZ2', 'Bronze 2', 'bronze 2', 'BRONZE 2', 'Bronze2', 'bronze2', 'BRONZE2']
rank6 = ['B 3', 'b 3', 'B3', 'b3', 'Br 3', 'br 3', 'BR 3', 'Br3', 'br3', 'BR3', 'Bz 3', 'bz 3', 'BZ 3', 'Bz3', 'bz3', 'BZ3', 'Brz 3', 'brz 3', 'BRZ 3', 'Brz3', 'brz3', 'BRZ3', 'Bronze 3', 'bronze 3', 'BRONZE 3', 'Bronze3', 'bronze3', 'BRONZE3']
rank7 = ['S 1', 's 1', 'S1', 's1', 'Sl 1', 'sl 1', 'SL 1', 'Sl1', 'sl1', 'SL1', 'Sv 1', 'sv 1', 'SV 1', 'Sv1', 'sv1', 'SV1', 'Slv 1', 'slv 1', 'SLV 1', 'Slv1', 'slv1', 'SLV1', 'Silver 1', 'silver 1', 'SILVER 1', 'Silver1', 'silver1', 'SILVER1']
rank8 = ['S 2', 's 2', 'S2', 's2', 'Sl 2', 'sl 2', 'SL 2', 'Sl2', 'sl2', 'SL2', 'Sv 2', 'sv 2', 'SV 2', 'Sv2', 'sv2', 'SV2', 'Slv 2', 'slv 2', 'SLV 2', 'Slv2', 'slv2', 'SLV2', 'Silver 2', 'silver 2', 'SILVER 2', 'Silver2', 'silver2', 'SILVER2']
rank9 = ['S 3', 's 3', 'S3', 's3', 'Sl 3', 'sl 3', 'SL 3', 'Sl3', 'sl3', 'SL3', 'Sv 3', 'sv 3', 'SV 3', 'Sv3', 'sv3', 'SV3', 'Slv 3', 'slv 3', 'SLV 3', 'Slv3', 'slv3', 'SLV3', 'Silver 3', 'silver 3', 'SILVER 3', 'Silver3', 'silver3', 'SILVER3']
rank10 = ['G 1', 'g 1', 'G1', 'g1', 'Gl 1', 'gl 1', 'GL 1', 'Gl1', 'gl1', 'GL1', 'Gd 1', 'gd 1', 'GD 1', 'Gd1', 'gd1', 'GD1', 'Gld 1', 'gld 1', 'GLD 1', 'Gld1', 'gld1', 'GLD1', 'Gold 1', 'gold 1', 'GOLD 1', 'Gold1', 'gold1', 'GOLD1']
rank11 = ['G 2', 'g 2', 'G2', 'g2', 'Gl 2', 'gl 2', 'GL 2', 'Gl2', 'gl2', 'GL2', 'Gd 2', 'gd 2', 'GD 2', 'Gd2', 'gd2', 'GD2', 'Gld 2', 'gld 2', 'GLD 2', 'Gld2', 'gld2', 'GLD2', 'Gold 2', 'gold 2', 'GOLD 2', 'Gold2', 'gold2', 'GOLD2']
rank12 = ['G 3', 'g 3', 'G3', 'g3', 'Gl 3', 'gl 3', 'GL 3', 'Gl3', 'gl3', 'GL3', 'Gd 3', 'gd 3', 'GD 3', 'Gd3', 'gd3', 'GD3', 'Gld 3', 'gld 3', 'GLD 3', 'Gld3', 'gld3', 'GLD3', 'Gold 3', 'gold 3', 'GOLD 3', 'Gold3', 'gold3', 'GOLD3']
rank13 = ['P 1', 'p 1', 'P1', 'p1', 'Pl 1', 'pl 1', 'PL 1', 'Pl1', 'pl1', 'PL1', 'Pt 1', 'pt 1', 'PT 1', 'Pt1', 'pt1', 'PT1', 'Plt 1', 'plt 1', 'PLT 1', 'Plt1', 'plt1', 'PLT1', 'Platinum 1', 'platinum 1', 'PLATINUM 1', 'Platinum1', 'platinum1', 'PLATINUM1']
rank14 = ['P 2', 'p 2', 'P2', 'p2', 'Pl 2', 'pl 2', 'PL 2', 'Pl2', 'pl2', 'PL2', 'Pt 2', 'pt 2', 'PT 2', 'Pt2', 'pt2', 'PT2', 'Plt 2', 'plt 2', 'PLT 2', 'Plt2', 'plt2', 'PLT2', 'Platinum 2', 'platinum 2', 'PLATINUM 2', 'Platinum2', 'platinum2', 'PLATINUM2']
rank15 = ['P 3', 'p 3', 'P3', 'p3', 'Pl 3', 'pl 3', 'PL 3', 'Pl3', 'pl3', 'PL3', 'Pt 3', 'pt 3', 'PT 3', 'Pt3', 'pt3', 'PT3', 'Plt 3', 'plt 3', 'PLT 3', 'Plt3', 'plt3', 'PLT3', 'Platinum 3', 'platinum 3', 'PLATINUM 3', 'Platinum3', 'platinum3', 'PLATINUM3']
rank16 = ['D 1', 'd 1', 'D1', 'd1', 'Di 1', 'di 1', 'DI 1', 'Di1', 'di1', 'DI1', 'Dm 1', 'dm 1', 'DM 1', 'Dm1', 'dm1', 'DM1', 'Dmd 1', 'dmd 1', 'DMD 1', 'Dmd1', 'dmd1', 'DMD1', 'Diamond 1', 'diamond 1', 'DIAMOND 1', 'Diamond1', 'diamond1', 'DIAMOND1']
rank17 = ['D 2', 'd 2', 'D2', 'd2', 'Di 2', 'di 2', 'DI 2', 'Di2', 'di2', 'DI2', 'Dm 2', 'dm 2', 'DM 2', 'Dm2', 'dm2', 'DM2', 'Dmd 2', 'dmd 2', 'DMD 2', 'Dmd2', 'dmd2', 'DMD2', 'Diamond 2', 'diamond 2', 'DIAMOND 2', 'Diamond2', 'diamond2', 'DIAMOND2']
rank18 = ['D 3', 'd 3', 'D3', 'd3', 'Di 3', 'di 3', 'DI 3', 'Di3', 'di3', 'DI3', 'Dm 3', 'dm 3', 'DM 3', 'Dm3', 'dm3', 'DM3', 'Dmd 3', 'dmd 3', 'DMD 3', 'Dmd3', 'dmd3', 'DMD3', 'Diamond 3', 'diamond 3', 'DIAMOND 3', 'Diamond3', 'diamond3', 'DIAMOND3']
rank19 = ['Im 1', 'im 1', 'IM 1', 'Im1', 'im1', 'IM1', 'Il 1', 'il 1', 'IL 1', 'Il1', 'il1', 'IL1', 'Imm 1', 'imm 1', 'IMM 1', 'Imm1', 'imm1', 'IMM1', 'Immortal 1', 'immortal 1', 'IMMORTAL 1', 'Immortal1', 'immortal1', 'IMMORTAL1']
rank20 = ['Im 2', 'im 2', 'IM 2', 'Im2', 'im2', 'IM2', 'Il 2', 'il 2', 'IL 2', 'Il2', 'il2', 'IL2', 'Imm 2', 'imm 2', 'IMM 2', 'Imm2', 'imm2', 'IMM2', 'Immortal 2', 'immortal 2', 'IMMORTAL 2', 'Immortal2', 'immortal2', 'IMMORTAL2']
rank21 = ['Im 3', 'im 3', 'IM 3', 'Im3', 'im3', 'IM3', 'Il 3', 'il 3', 'IL 3', 'Il3', 'il3', 'IL3', 'Imm 3', 'imm 3', 'IMM 3', 'Imm3', 'imm3', 'IMM3', 'Immortal 3', 'immortal 3', 'IMMORTAL 3', 'Immortal3', 'immortal3', 'IMMORTAL3']
rank22 = ['R', 'r', 'Rd', 'rd', 'RD', 'Rt', 'rt', 'RT', 'Rad', 'rad', 'RAD', 'Rdt', 'rdt', 'RDT', 'Rnt', 'rnt', 'RNT', 'Radiant', 'radiant', 'RADIANT']

# Naming Points

score1 = 4.5
score2 = 9.0
score3 = 13.5
score4 = 18.0
score5 = 22.5
score6 = 27.0
score7 = 31.5
score8 = 36.0
score9 = 40.5
score10 = 45.0
score11 = 49.5
score12 = 54.0
score13 = 58.5
score14 = 63.0
score15 = 67.5
score16 = 72.0
score17 = 76.5
score18 = 81.0
score19 = 85.5
score20 = 90.0
score21 = 94.5
score22 = 100.0

# Welcome

print('''Welcome to ValorantRevisor!

There is 22 Ranks in the game:

Iron 1, Iron 2, Iron 3

Bronze 1, Bronze 2, Bronze 3

Silver 1, Silver 2, Silver 3

Gold 1, Gold 2, Gold 3

Platinum 1, Platinum 2, Platinum 3

Diamond 1, Diamond 2, Diamond 3

Immortal 1, Immortal 2, Immortal 3

Radiant

So each Rank is about 4.5 abstract points. Those points making the Team Score.

ValorantRevisor will count your and your enemies Team Score and tell You were your games fair or not.

Remember that Iron and Immortal Ranks starts from same letter so if You want to wright Immortal Rank shorthand use "Im" instead of just "I" because that is for Iron Ranks!''')

# Read Ranks and counting Team Score

while True:

# Ally Ranks

    allyrank1 = input('\nEnter fist Teammate Rank: ')
    if allyrank1 not in allranks:
        out = input('\nWrong Rank(maybe You entered a non-existent shorthand)! Try Again? Y/N: ').lower()
        if out == 'y':
            continue
        else:
            break
    else:
        if allyrank1 in rank1:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Iron 1(4.5 points)', file=f)
            allyrank1 = score1
        if allyrank1 in rank2:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Iron 2(9 points)', file=f)
            allyrank1 = score2
        if allyrank1 in rank3:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Iron 3(13.5 points)', file=f)
            allyrank1 = score3
        if allyrank1 in rank4:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Bronze 1(18 points)', file=f)
            allyrank1 = score4
        if allyrank1 in rank5:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Bronze 2(22.5 points)', file=f)
            allyrank1 = score5
        if allyrank1 in rank6:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Bronze 3(27 points)', file=f)
            allyrank1 = score6
        if allyrank1 in rank7:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Silver 1(31.5 points)', file=f)
            allyrank1 = score7
        if allyrank1 in rank8:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Silver 2(36 points)', file=f)
            allyrank1 = score8
        if allyrank1 in rank9:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Silver 3(40.5 points)', file=f)
            allyrank1 = score9
        if allyrank1 in rank10:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Gold 1(45 points)', file=f)
            allyrank1 = score10
        if allyrank1 in rank11:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Gold 2(49.5 points)', file=f)
            allyrank1 = score11
        if allyrank1 in rank12:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Gold 3(54 points)', file=f)
            allyrank1 = score12
        if allyrank1 in rank13:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Platinum 1(58.5 points)', file=f)
            allyrank1 = score13
        if allyrank1 in rank14:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Platinum 2(63 points)', file=f)
            allyrank1 = score14
        if allyrank1 in rank15:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Platinum 3(67.5 points)', file=f)
            allyrank1 = score15
        if allyrank1 in rank16:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Diamond 1(72 points)', file=f)
            allyrank1 = score16
        if allyrank1 in rank17:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Diamond 2(76.5 points)', file=f)
            allyrank1 = score17
        if allyrank1 in rank18:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Diamond 3(81 points)', file=f)
            allyrank1 = score18
        if allyrank1 in rank19:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Immortal 1(85.5 points)', file=f)
            allyrank1 = score19
        if allyrank1 in rank20:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Immortal 2(90 points)', file=f)
            allyrank1 = score20
        if allyrank1 in rank21:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Immortal 3(94.5 points)', file=f)
            allyrank1 = score21
        if allyrank1 in rank22:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Ally Rank is: Radiant(100 points)', file=f)
            allyrank1 = score22

    allyrank2 = input('\nEnter second Teammate Rank: ')
    if allyrank2 not in allranks:
        out = input('\nWrong Rank(maybe You entered a non-existent shorthand)! Try Again? Y/N: ').lower()
        if out == 'y':
            continue
        else:
            break
    else:
        if allyrank2 in rank1:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Iron 1(4.5 points)', file=f)
            allyrank2 = score1
        if allyrank2 in rank2:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Iron 2(9 points)', file=f)
            allyrank2 = score2
        if allyrank2 in rank3:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Iron 3(13.5 points)', file=f)
            allyrank2 = score3
        if allyrank2 in rank4:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Bronze 1(18 points)', file=f)
            allyrank2 = score4
        if allyrank2 in rank5:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Bronze 2(22.5 points)', file=f)
            allyrank2 = score5
        if allyrank2 in rank6:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Bronze 3(27 points)', file=f)
            allyrank2 = score6
        if allyrank2 in rank7:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('Second Ally Rank is: Silver 1(31.5 points)', file=f)
            allyrank2 = score7
        if allyrank2 in rank8:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Silver 2(36 points)', file=f)
            allyrank2 = score8
        if allyrank2 in rank9:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Silver 3(40.5 points)', file=f)
            allyrank2 = score9
        if allyrank2 in rank10:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Gold 1(45 points)', file=f)
            allyrank2 = score10
        if allyrank2 in rank11:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Gold 2(49.5 points)', file=f)
            allyrank2 = score11
        if allyrank2 in rank12:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Gold 3(54 points)', file=f)
            allyrank2 = score12
        if allyrank2 in rank13:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Platinum 1(58.5 points)', file=f)
            allyrank2 = score13
        if allyrank2 in rank14:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Platinum 2(63 points)', file=f)
            allyrank2 = score14
        if allyrank2 in rank15:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Platinum 3(67.5 points)', file=f)
            allyrank2 = score15
        if allyrank2 in rank16:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Diamond 1(72 points)', file=f)
            allyrank2 = score16
        if allyrank2 in rank17:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Diamond 2(76.5 points)', file=f)
            allyrank2 = score17
        if allyrank2 in rank18:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Diamond 3(81 points)', file=f)
            allyrank2 = score18
        if allyrank2 in rank19:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Immortal 1(85.5 points)', file=f)
            allyrank2 = score19
        if allyrank2 in rank20:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Immortal 2(90 points)', file=f)
            allyrank2 = score20
        if allyrank2 in rank21:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Immortal 3(94.5 points)', file=f)
            allyrank2 = score21
        if allyrank2 in rank22:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Ally Rank is: Radiant(100 points)', file=f)
            allyrank2 = score22

    allyrank3 = input('\nEnter third Teammate Rank: ')
    if allyrank3 not in allranks:
        out = input('\nWrong Rank(maybe You entered a non-existent shorthand)! Try Again? Y/N: ').lower()
        if out == 'y':
            continue
        else:
            break
    else:
        if allyrank3 in rank1:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Iron 1(4.5 points)', file=f)
            allyrank3 = score1
        if allyrank3 in rank2:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Iron 2(9 points)', file=f)
            allyrank3 = score2
        if allyrank3 in rank3:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Iron 3(13.5 points)', file=f)
            allyrank3 = score3
        if allyrank3 in rank4:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Bronze 1(18 points)', file=f)
            allyrank3 = score4
        if allyrank3 in rank5:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Bronze 2(22.5 points)', file=f)
            allyrank3 = score5
        if allyrank3 in rank6:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Bronze 3(27 points)', file=f)
            allyrank3 = score6
        if allyrank3 in rank7:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Silver 1(31.5 points)', file=f)
            allyrank3 = score7
        if allyrank3 in rank8:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Silver 2(36 points)', file=f)
            allyrank3 = score8
        if allyrank3 in rank9:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Silver 3(40.5 points)', file=f)
            allyrank3 = score9
        if allyrank3 in rank10:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Gold 1(45 points)', file=f)
            allyrank3 = score10
        if allyrank3 in rank11:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Gold 2(49.5 points)', file=f)
            allyrank3 = score11
        if allyrank3 in rank12:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Gold 3(54 points)', file=f)
            allyrank3 = score12
        if allyrank3 in rank13:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Platinum 1(58.5 points)', file=f)
            allyrank3 = score13
        if allyrank3 in rank14:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Platinum 2(63 points)', file=f)
            allyrank3 = score14
        if allyrank3 in rank15:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Platinum 3(67.5 points)', file=f)
            allyrank3 = score15
        if allyrank3 in rank16:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Diamond 1(72 points)', file=f)
            allyrank3 = score16
        if allyrank3 in rank17:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Diamond 2(76.5 points)', file=f)
            allyrank3 = score17
        if allyrank3 in rank18:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Diamond 3(81 points)', file=f)
            allyrank3 = score18
        if allyrank3 in rank19:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Immortal 1(85.5 points)', file=f)
            allyrank3 = score19
        if allyrank3 in rank20:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Immortal 2(90 points)', file=f)
            allyrank3 = score20
        if allyrank3 in rank21:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Immortal 3(94.5 points)', file=f)
            allyrank3 = score21
        if allyrank3 in rank22:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Ally Rank is: Radiant(100 points)', file=f)
            allyrank3 = score22

    allyrank4 = input('\nEnter fourth Teammate Rank: ')
    if allyrank4 not in allranks:
        out = input('\nWrong Rank(maybe You entered a non-existent shorthand)! Try Again? Y/N: ').lower()
        if out == 'y':
            continue
        else:
            break
    else:
        if allyrank4 in rank1:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Iron 1(4.5 points)', file=f)
            allyrank4 = score1
        if allyrank4 in rank2:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Iron 2(9 points)', file=f)
            allyrank4 = score2
        if allyrank4 in rank3:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Iron 3(13.5 points)', file=f)
            allyrank4 = score3
        if allyrank4 in rank4:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Bronze 1(18 points)', file=f)
            allyrank4 = score4
        if allyrank4 in rank5:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Bronze 2(22.5 points)', file=f)
            allyrank4 = score5
        if allyrank4 in rank6:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Bronze 3(27 points)', file=f)
            allyrank4 = score6
        if allyrank4 in rank7:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Silver 1(31.5 points)', file=f)
            allyrank4 = score7
        if allyrank4 in rank8:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Silver 2(36 points)', file=f)
            allyrank4 = score8
        if allyrank4 in rank9:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Silver 3(40.5 points)', file=f)
            allyrank4 = score9
        if allyrank4 in rank10:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Gold 1(45 points)', file=f)
            allyrank4 = score10
        if allyrank4 in rank11:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Gold 2(49.5 points)', file=f)
            allyrank4 = score11
        if allyrank4 in rank12:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Gold 3(54 points)', file=f)
            allyrank4 = score12
        if allyrank4 in rank13:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Platinum 1(58.5 points)', file=f)
            allyrank4 = score13
        if allyrank4 in rank14:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Platinum 2(63 points)', file=f)
            allyrank4 = score14
        if allyrank4 in rank15:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Platinum 3(67.5 points)', file=f)
            allyrank4 = score15
        if allyrank4 in rank16:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Diamond 1(72 points)', file=f)
            allyrank4 = score16
        if allyrank4 in rank17:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Diamond 2(76.5 points)', file=f)
            allyrank4 = score17
        if allyrank4 in rank18:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Diamond 3(81 points)', file=f)
            allyrank4 = score18
        if allyrank4 in rank19:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Immortal 1(85.5 points)', file=f)
            allyrank4 = score19
        if allyrank4 in rank20:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Immortal 2(90 points)', file=f)
            allyrank4 = score20
        if allyrank4 in rank21:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Immortal 3(94.5 points)', file=f)
            allyrank4 = score21
        if allyrank4 in rank22:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Ally Rank is: Radiant(100 points)', file=f)
            allyrank4 = score22

    allyrank5 = input('\nEnter fifth Teammate Rank: ')
    if allyrank5 not in allranks:
        out = input('\nWrong Rank(maybe You entered a non-existent shorthand)! Try Again? Y/N: ').lower()
        if out == 'y':
            continue
        else:
            break
    else:
        if allyrank5 in rank1:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Iron 1(4.5 points)', file=f)
            allyrank5 = score1
        if allyrank5 in rank2:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Iron 2(9 points)', file=f)
            allyrank5 = score2
        if allyrank5 in rank3:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Iron 3(13.5 points)', file=f)
            allyrank5 = score3
        if allyrank5 in rank4:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Bronze 1(18 points)', file=f)
            allyrank5 = score4
        if allyrank5 in rank5:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Bronze 2(22.5 points)', file=f)
            allyrank5 = score5
        if allyrank5 in rank6:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Bronze 3(27 points)', file=f)
            allyrank5 = score6
        if allyrank5 in rank7:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Silver 1(31.5 points)', file=f)
            allyrank5 = score7
        if allyrank5 in rank8:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Silver 2(36 points)', file=f)
            allyrank5 = score8
        if allyrank5 in rank9:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Silver 3(40.5 points)', file=f)
            allyrank5 = score9
        if allyrank5 in rank10:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Gold 1(45 points)', file=f)
            allyrank5 = score10
        if allyrank5 in rank11:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Gold 2(49.5 points)', file=f)
            allyrank5 = score11
        if allyrank5 in rank12:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Gold 3(54 points)', file=f)
            allyrank5 = score12
        if allyrank5 in rank13:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Platinum 1(58.5 points)', file=f)
            allyrank5 = score13
        if allyrank5 in rank14:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Platinum 2(63 points)', file=f)
            allyrank5 = score14
        if allyrank5 in rank15:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Platinum 3(67.5 points)', file=f)
            allyrank5 = score15
        if allyrank5 in rank16:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Diamond 1(72 points)', file=f)
            allyrank5 = score16
        if allyrank5 in rank17:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Diamond 2(76.5 points)', file=f)
            allyrank5 = score17
        if allyrank5 in rank18:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Diamond 3(81 points)', file=f)
            allyrank5 = score18
        if allyrank5 in rank19:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Immortal 1(85.5 points)', file=f)
            allyrank5 = score19
        if allyrank5 in rank20:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Immortal 2(90 points)', file=f)
            allyrank5 = score20
        if allyrank5 in rank21:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Immortal 3(94.5 points)', file=f)
            allyrank5 = score21
        if allyrank5 in rank22:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Ally Rank is: Radiant(100 points)', file=f)
            allyrank5 = score22

# Enemy Ranks

    enemyrank1 = input('\nEnter first Enemy Rank: ')
    if enemyrank1 not in allranks:
        out = input('\nWrong Rank(maybe You entered a non-existent shorthand)! Try Again? Y/N: ').lower()
        if out == 'y':
            continue
        else:
            break
    else:
        if enemyrank1 in rank1:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Iron 1(4.5 points)', file=f)
            enemyrank1 = score1
        if enemyrank1 in rank2:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Iron 2(9 points)', file=f)
            enemyrank1 = score2
        if enemyrank1 in rank3:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Iron 3(13.5 points)', file=f)
            enemyrank1 = score3
        if enemyrank1 in rank4:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Bronze 1(18 points)', file=f)
            enemyrank1 = score4
        if enemyrank1 in rank5:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Bronze 2(22.5 points)', file=f)
            enemyrank1 = score5
        if enemyrank1 in rank6:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Bronze 3(27 points)', file=f)
            enemyrank1 = score6
        if enemyrank1 in rank7:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Silver 1(31.5 points)', file=f)
            enemyrank1 = score7
        if enemyrank1 in rank8:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Silver 2(36 points)', file=f)
            enemyrank1 = score8
        if enemyrank1 in rank9:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Silver 3(40.5 points)', file=f)
            enemyrank1 = score9
        if enemyrank1 in rank10:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Gold 1(45 points)', file=f)
            enemyrank1 = score10
        if enemyrank1 in rank11:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Gold 2(49.5 points)', file=f)
            enemyrank1 = score11
        if enemyrank1 in rank12:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Gold 3(54 points)', file=f)
            enemyrank1 = score12
        if enemyrank1 in rank13:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Platinum 1(58.5 points)', file=f)
            enemyrank1 = score13
        if enemyrank1 in rank14:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Platinum 2(63 points)', file=f)
            enemyrank1 = score14
        if enemyrank1 in rank15:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Platinum 3(67.5 points)', file=f)
            enemyrank1 = score15
        if enemyrank1 in rank16:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Diamond 1(72 points)', file=f)
            enemyrank1 = score16
        if enemyrank1 in rank17:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Diamond 2(76.5 points)', file=f)
            enemyrank1 = score17
        if enemyrank1 in rank18:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Diamond 3(81 points)', file=f)
            enemyrank1 = score18
        if enemyrank1 in rank19:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Immortal 1(85.5 points)', file=f)
            enemyrank1 = score19
        if enemyrank1 in rank20:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Immortal 2(90 points)', file=f)
            enemyrank1 = score20
        if enemyrank1 in rank21:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Immortal 3(94.5 points)', file=f)
            enemyrank1 = score21
        if enemyrank1 in rank22:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\n\nFirst Enemy Rank is: Radiant(100 points)', file=f)
            enemyrank1 = score22

    enemyrank2 = input('\nEnter second Enemy Rank: ')
    if enemyrank2 not in allranks:
        out = input('\nWrong Rank(maybe You entered a non-existent shorthand)! Try Again? Y/N: ').lower()
        if out == 'y':
            continue
        else:
            break
    else:
        if enemyrank2 in rank1:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Iron 1(4.5 points)', file=f)
            enemyrank2 = score1
        if enemyrank2 in rank2:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Iron 2(9 points)', file=f)
            enemyrank2 = score2
        if enemyrank2 in rank3:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Iron 3(13.5 points)', file=f)
            enemyrank2 = score3
        if enemyrank2 in rank4:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Bronze 1(18 points)', file=f)
            enemyrank2 = score4
        if enemyrank2 in rank5:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Bronze 2(22.5 points)', file=f)
            enemyrank2 = score5
        if enemyrank2 in rank6:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Bronze 3(27 points)', file=f)
            enemyrank2 = score6
        if enemyrank2 in rank7:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Silver 1(31.5 points)', file=f)
            enemyrank2 = score7
        if enemyrank2 in rank8:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Silver 2(36 points)', file=f)
            enemyrank2 = score8
        if enemyrank2 in rank9:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Silver 3(40.5 points)', file=f)
            enemyrank2 = score9
        if enemyrank2 in rank10:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Gold 1(45 points)', file=f)
            enemyrank2 = score10
        if enemyrank2 in rank11:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Gold 2(49.5 points)', file=f)
            enemyrank2 = score11
        if enemyrank2 in rank12:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Gold 3(54 points)', file=f)
            enemyrank2 = score12
        if enemyrank2 in rank13:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Platinum 1(58.5 points)', file=f)
            enemyrank2 = score13
        if enemyrank2 in rank14:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Platinum 2(63 points)', file=f)
            enemyrank2 = score14
        if enemyrank2 in rank15:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Platinum 3(67.5 points)', file=f)
            enemyrank2 = score15
        if enemyrank2 in rank16:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Diamond 1(72 points)', file=f)
            enemyrank2 = score16
        if enemyrank2 in rank17:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Diamond 2(76.5 points)', file=f)
            enemyrank2 = score17
        if enemyrank2 in rank18:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Diamond 3(81 points)', file=f)
            enemyrank2 = score18
        if enemyrank2 in rank19:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('Second Enemy Rank is: Immortal 1(85.5 points)', file=f)
            enemyrank2 = score19
        if enemyrank2 in rank20:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Immortal 2(90 points)', file=f)
            enemyrank2 = score20
        if enemyrank2 in rank21:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Immortal 3(94.5 points)', file=f)
            enemyrank2 = score21
        if enemyrank2 in rank22:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nSecond Enemy Rank is: Radiant(100 points)', file=f)
            enemyrank2 = score22

    enemyrank3 = input('\nEnter third Enemy Rank: ')
    if enemyrank3 not in allranks:
        out = input('\nWrong Rank(maybe You entered a non-existent shorthand)! Try Again? Y/N: ').lower()
        if out == 'y':
            continue
        else:
            break
    else:
        if enemyrank3 in rank1:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Iron 1(4.5 points)', file=f)
            enemyrank3 = score1
        if enemyrank3 in rank2:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Iron 2(9 points)', file=f)
            enemyrank3 = score2
        if enemyrank3 in rank3:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Iron 3(13.5 points)', file=f)
            enemyrank3 = score3
        if enemyrank3 in rank4:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Bronze 1(18 points)', file=f)
            enemyrank3 = score4
        if enemyrank3 in rank5:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Bronze 2(22.5 points)', file=f)
            enemyrank3 = score5
        if enemyrank3 in rank6:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Bronze 3(27 points)', file=f)
            enemyrank3 = score6
        if enemyrank3 in rank7:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Silver 1(31.5 points)', file=f)
            enemyrank3 = score7
        if enemyrank3 in rank8:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Silver 2(36 points)', file=f)
            enemyrank3 = score8
        if enemyrank3 in rank9:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Silver 3(40.5 points)', file=f)
            enemyrank3 = score9
        if enemyrank3 in rank10:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Gold 1(45 points)', file=f)
            enemyrank3 = score10
        if enemyrank3 in rank11:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Gold 2(49.5 points)', file=f)
            enemyrank3 = score11
        if enemyrank3 in rank12:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Gold 3(54 points)', file=f)
            enemyrank3 = score12
        if enemyrank3 in rank13:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Platinum 1(58.5 points)', file=f)
            enemyrank3 = score13
        if enemyrank3 in rank14:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Platinum 2(63 points)', file=f)
            enemyrank3 = score14
        if enemyrank3 in rank15:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Platinum 3(67.5 points)', file=f)
            enemyrank3 = score15
        if enemyrank3 in rank16:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Diamond 1(72 points)', file=f)
            enemyrank3 = score16
        if enemyrank3 in rank17:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Diamond 2(76.5 points)', file=f)
            enemyrank3 = score17
        if enemyrank3 in rank18:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Diamond 3(81 points)', file=f)
            enemyrank3 = score18
        if enemyrank3 in rank19:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Immortal 1(85.5 points)', file=f)
            enemyrank3 = score19
        if enemyrank3 in rank20:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Immortal 2(90 points)', file=f)
            enemyrank3 = score20
        if enemyrank3 in rank21:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Immortal 3(94.5 points)', file=f)
            enemyrank3 = score21
        if enemyrank3 in rank22:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nThird Enemy Rank is: Radiant(100 points)', file=f)
            enemyrank3 = score22

    enemyrank4 = input('\nEnter fourth Enemy Rank: ')
    if enemyrank4 not in allranks:
        out = input('\nWrong Rank(maybe You entered a non-existent shorthand)! Try Again? Y/N: ').lower()
        if out == 'y':
            continue
        else:
            break
    else:
        if enemyrank4 in rank1:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Iron 1(4.5 points)', file=f)
            enemyrank4 = score1
        if enemyrank4 in rank2:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Iron 2(9 points)', file=f)
            enemyrank4 = score2
        if enemyrank4 in rank3:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Iron 3(13.5 points)', file=f)
            enemyrank4 = score3
        if enemyrank4 in rank4:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Bronze 1(18 points)', file=f)
            enemyrank4 = score4
        if enemyrank4 in rank5:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Bronze 2(22.5 points)', file=f)
            enemyrank4 = score5
        if enemyrank4 in rank6:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Bronze 3(27 points)', file=f)
            enemyrank4 = score6
        if enemyrank4 in rank7:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Silver 1(31.5 points)', file=f)
            enemyrank4 = score7
        if enemyrank4 in rank8:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Silver 2(36 points)', file=f)
            enemyrank4 = score8
        if enemyrank4 in rank9:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Silver 3(40.5 points)', file=f)
            enemyrank4 = score9
        if enemyrank4 in rank10:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Gold 1(45 points)', file=f)
            enemyrank4 = score10
        if enemyrank4 in rank11:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Gold 2(49.5 points)', file=f)
            enemyrank4 = score11
        if enemyrank4 in rank12:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Gold 3(54 points)', file=f)
            enemyrank4 = score12
        if enemyrank4 in rank13:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Platinum 1(58.5 points)', file=f)
            enemyrank4 = score13
        if enemyrank4 in rank14:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Platinum 2(63 points)', file=f)
            enemyrank4 = score14
        if enemyrank4 in rank15:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Platinum 3(67.5 points)', file=f)
            enemyrank4 = score15
        if enemyrank4 in rank16:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Diamond 1(72 points)', file=f)
            enemyrank4 = score16
        if enemyrank4 in rank17:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Diamond 2(76.5 points)', file=f)
            enemyrank4 = score17
        if enemyrank4 in rank18:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Diamond 3(81 points)', file=f)
            enemyrank4 = score18
        if enemyrank4 in rank19:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Immortal 1(85.5 points)', file=f)
            enemyrank4 = score19
        if enemyrank4 in rank20:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Immortal 2(90 points)', file=f)
            enemyrank4 = score20
        if enemyrank4 in rank21:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Immortal 3(94.5 points)', file=f)
            enemyrank4 = score21
        if enemyrank4 in rank22:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFourth Enemy Rank is: Radiant(100 points)', file=f)
            enemyrank4 = score22

    enemyrank5 = input('\nEnter fifth Enemy Rank: ')
    if enemyrank5 not in allranks:
        out = input('\nWrong Rank(maybe You entered a non-existent shorthand)! Try Again? Y/N: ').lower()
        if out == 'y':
            continue
        else:
            break
    else:
        if enemyrank5 in rank1:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Iron 1(4.5 points)', file=f)
            enemyrank5 = score1
        if enemyrank5 in rank2:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Iron 2(9 points)', file=f)
            enemyrank5 = score2
        if enemyrank5 in rank3:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Iron 3(13.5 points)', file=f)
            enemyrank5 = score3
        if enemyrank5 in rank4:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Bronze 1(18 points)', file=f)
            enemyrank5 = score4
        if enemyrank5 in rank5:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Bronze 2(22.5 points)', file=f)
            enemyrank5 = score5
        if enemyrank5 in rank6:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Bronze 3(27 points)', file=f)
            enemyrank5 = score6
        if enemyrank5 in rank7:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Silver 1(31.5 points)', file=f)
            enemyrank5 = score7
        if enemyrank5 in rank8:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Silver 2(36 points)', file=f)
            enemyrank5 = score8
        if enemyrank5 in rank9:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Silver 3(40.5 points)', file=f)
            enemyrank5 = score9
        if enemyrank5 in rank10:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Gold 1(45 points)', file=f)
            enemyrank5 = score10
        if enemyrank5 in rank11:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Gold 2(49.5 points)', file=f)
            enemyrank5 = score11
        if enemyrank5 in rank12:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Gold 3(54 points)', file=f)
            enemyrank5 = score12
        if enemyrank5 in rank13:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Platinum 1(58.5 points)', file=f)
            enemyrank5 = score13
        if enemyrank5 in rank14:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Platinum 2(63 points)', file=f)
            enemyrank5 = score14
        if enemyrank5 in rank15:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Platinum 3(67.5 points)', file=f)
            enemyrank5 = score15
        if enemyrank5 in rank16:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Diamond 1(72 points)', file=f)
            enemyrank5 = score16
        if enemyrank5 in rank17:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Diamond 2(76.5 points)', file=f)
            enemyrank5 = score17
        if enemyrank5 in rank18:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Diamond 3(81 points)', file=f)
            enemyrank5 = score18
        if enemyrank5 in rank19:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Immortal 1(85.5 points)', file=f)
            enemyrank5 = score19
        if enemyrank5 in rank20:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Immortal 2(90 points)', file=f)
            enemyrank5 = score20
        if enemyrank5 in rank21:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Immortal 3(94.5 points)', file=f)
            enemyrank5 = score21
        if enemyrank5 in rank22:
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nFifth Enemy Rank is: Radiant(100 points)', file=f)
            enemyrank5 = score22

# Team Score, Team Difference and Game Result

        AllyTeamScore = (allyrank1 + allyrank2 + allyrank3 + allyrank4 + allyrank5)

        EnemyTeamScore = (enemyrank1 + enemyrank2 + enemyrank3 + enemyrank4 + enemyrank5)

        if AllyTeamScore > EnemyTeamScore:
            TeamDiff = AllyTeamScore - EnemyTeamScore
            gameresult = input('\nDid You win? Y/N: ').lower()
            if gameresult == 'y':
                dateandtime = date.strftime('\n%H:%M:%S on %A, %B the %dth, %Y \nW O N')
                print(dateandtime)
                print('\nYour Team Score is:',AllyTeamScore,'points.\nEnemy Team Score is:',EnemyTeamScore,'points.\nTeam Difference is:',TeamDiff,'points in your favour.')
                with open('ValorantRevisorLogs.txt', 'a+') as f:
                    print(dateandtime,'\nYour Team Score is:',AllyTeamScore,'points.\nEnemy Team Score is:',EnemyTeamScore,'points.\nTeam Difference is:',TeamDiff,'points in your favour.', file=f)
            if gameresult == 'n':
                dateandtime = date.strftime('\n%H:%M:%S on %A, %B the %dth, %Y \nL O S T')
                print(dateandtime)
                print('\nYour Team Score is:',AllyTeamScore,'points.\nEnemy Team Score is:',EnemyTeamScore,'points.\nTeam Difference is:',TeamDiff,'points in your favour.')
                with open('ValorantRevisorLogs.txt', 'a+') as f:
                    print(dateandtime,'\nYour Team Score is:',AllyTeamScore,'points.\nEnemy Team Score is:',EnemyTeamScore,'points.\nTeam Difference is:',TeamDiff,'points in your favour.', file=f)
        if EnemyTeamScore > AllyTeamScore:
            TeamDiff = EnemyTeamScore - AllyTeamScore
            gameresult = input('\nDid You win? Y/N: ').lower()
            if gameresult == 'y':
                dateandtime = date.strftime('\n%H:%M:%S on %A, %B the %dth, %Y \nW O N')
                print(dateandtime)
                print('\nYour Team Score is:',AllyTeamScore,'points.\nEnemy Team Score is:',EnemyTeamScore,'points.\nTeam Difference is:',TeamDiff,'points in favour of enemies.')
                with open('ValorantRevisorLogs.txt', 'a+') as f:
                    print(dateandtime,'\nYour Team Score is:',AllyTeamScore,'points.\nEnemy Team Score is:',EnemyTeamScore,'points.\nTeam Difference is:',TeamDiff,'points in favour of enemies.', file=f)
            if gameresult == 'n':
                dateandtime = date.strftime('\n%H:%M:%S on %A, %B the %dth, %Y \nL O S T')
                print(dateandtime)
                print('\nYour Team Score is:',AllyTeamScore,'points.\nEnemy Team Score is:',EnemyTeamScore,'points.\nTeam Difference is:',TeamDiff,'points in favour of enemies.')
                with open('ValorantRevisorLogs.txt', 'a+') as f:
                    print(dateandtime,'\nYour Team Score is:',AllyTeamScore,'points.\nEnemy Team Score is:',EnemyTeamScore,'points.\nTeam Difference is:',TeamDiff,'points in favour of enemies.', file=f)
        if AllyTeamScore == EnemyTeamScore:
            TeamDiff = 0
            gameresult = input('\nDid You win? Y/N: ').lower()
            if gameresult == 'y':
                dateandtime = date.strftime('\n%H:%M:%S on %A, %B the %dth, %Y \nW O N')
                print(dateandtime)
                print('\nYour Team Score is:',AllyTeamScore,'points.\nEnemy Team Score is:',EnemyTeamScore,'points.\nTeam Difference is:',TeamDiff,'points.')
                with open('ValorantRevisorLogs.txt', 'a+') as f:
                    print(dateandtime,'\nYour Team Score is:',AllyTeamScore,'points.\nEnemy Team Score is:',EnemyTeamScore,'points.\nTeam Difference is:',TeamDiff,'points.', file=f)
            if gameresult == 'n':
                dateandtime = date.strftime('\n%H:%M:%S on %A, %B the %dth, %Y \nL O S T')
                print(dateandtime)
                print('\nYour Team Score is:',AllyTeamScore,'points.\nEnemy Team Score is:',EnemyTeamScore,'points.\nTeam Difference is:',TeamDiff,'points.')
                with open('ValorantRevisorLogs.txt', 'a+') as f:
                    print(dateandtime,'\nYour Team Score is:',AllyTeamScore,'points.\nEnemy Team Score is:',EnemyTeamScore,'points.\nTeam Difference is:',TeamDiff,'points.', file=f)
        if TeamDiff <= 4.5:
            print('\nGame was fair.')
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nGame was fair.', file=f)
        if 9 >= TeamDiff > 4.5:
            print('\nGame was slightly unfair !')
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nGame was slightly unfair !', file=f)
        if 13.5 >= TeamDiff > 9:
            print('\nGame was unfair ! !')
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nGame was unfair ! !', file=f)
        if TeamDiff > 13.5:
            print('\nGame was totally unfair ! ! !')
            with open('ValorantRevisorLogs.txt', 'a+') as f:
                print('\nGame was totally unfair ! ! !', file=f)
        break
print('\nThanks for using ValorantRevisor!')
input('\nEXIT ')