from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser


def get_main_args():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    arg = parser.add_argument
    # shp files
    arg("--east_africa_shp", type=str, default="F:/OSSDATA/Shapefiles/Dissolved/EasternAfrica.shp", help="East Africa Shapefile")
    arg("--south_africa_shp", type=str, default="F:/OSSDATA/Shapefiles/Dissolved/SouthAfrica.shp", help="South Africa Shapefile")
    arg("--north_africa_shp", type=str, default="F:/OSSDATA/Shapefiles/Dissolved/NorthAfrica.shp", help="North Africa Shapefile")
    arg("--west_africa_shp", type=str, default="F:/OSSDATA/Shapefiles/Dissolved/WesternAfrica.shp", help="West Africa Shapefile")
    arg("--central_africa_shp", type=str, default="F:/OSSDATA/Shapefiles/Dissolved/CentralAfrica.shp", help="Central Africa Shapefile")

    #forest mapographics
    arg("--forest_loss_dir", type=str, default=None, help="Forest Loss Directory")
    arg("--forest_cover_dir", type=str, default=None, help="Forest Cover Directory")
    arg("--forest_loss_mapographics_dir", type=str, default=None, help="Forest Loss Mapographics Directory")
    
    #land cover mapographics
    arg("--landcover_dir", type=str, default=None, help="Landcover Directory")
    arg("--landcover_mapographics_dir", type=str, default=None, help="Landcover Mapographics Directory")


    #land cover change mapographics
    arg("--landcover_change_dir", type=str, default=None, help="Landcover Change Directory")
    arg("--landcover_change_mapographics_dir", type=str, default=None, help="Landcover Change Mapographics Directory")



    return parser.parse_args()