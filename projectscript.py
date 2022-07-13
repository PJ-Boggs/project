import arcpy

# Create a new File Geo-database (fgdb) to both work from and store data
arcpy.CreateFileGDB_management("C:/Users/pjbog/project/DATA", "ReleaseSheet.gdb")

# Set new fgdb as workspace
arcpy.env.workspace = "C:/Users/pjbog/project/DATA/ReleaseSheet.gdb"
# Export Demand_Points file as a copy to work from
arcpy.FeatureClassToFeatureClass_conversion("Demand_Points", "C:/Users/pjbog/project/DATA/project.gdb", "ReleaseSheetPrems")
