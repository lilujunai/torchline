from torchline.config import CfgNode as CN

def add_skin_config(cfg):
    _C = cfg
    
    _C.loss.focal_loss.alpha = [3.32688889, 0.12486239, 3.05530612, 3.4025    , 3.32688889,
    0.21603175, 3.65146341, 2.10859155, 2.82471698, 4.40323529,
    1.05429577, 4.40323529, 2.02310811, 4.6784375 , 3.83871795,
    4.6784375 , 0.33642697, 0.06178704, 0.63978632, 2.87903846,
    0.67742081, 1.10080882, 0.38784974, 1.7208046 , 3.4025    ,
    4.15861111, 1.03965278, 3.32688889, 3.48162791, 1.59265957,
    1.74081395, 1.05429577, 3.05530612, 0.77569948, 3.93973684,
    0.55243542, 4.04621622, 2.87903846, 2.82471698, 2.23447761,
    2.5812069 , 4.40323529, 4.40323529, 2.02310811, 4.53666667,
    0.50070234, 0.850625  , 3.83871795, 3.25456522, 1.55947917,
    2.87903846, 4.15861111, 2.02310811, 4.15861111, 0.66537778,
    1.89506329, 1.4677451 , 3.48162791, 3.32688889, 3.48162791,
    2.62649123, 3.65146341, 1.89506329, 3.93973684, 3.74275   ,
    3.83871795, 0.50577703, 4.82935484, 1.16054264, 3.65146341,
    0.54638686, 2.67339286, 4.40323529, 1.80373494, 1.16960938,
    0.20396458, 2.9354902 , 2.49516667, 2.87903846, 1.66344444,
    0.68990783, 0.1684027 , 2.67339286, 1.05429577, 1.48227723,
    0.48765472, 1.14282443, 3.25456522, 2.5812069 , 2.722     ,
    0.51270548, 3.32688889, 2.41467742, 1.59265957, 0.63436441,
    1.27957265, 4.82935484, 4.40323529, 3.56452381, 4.40323529]
    _C.loss.focal_loss.gamma = 2
    _C.loss.focal_loss.size_average = True
