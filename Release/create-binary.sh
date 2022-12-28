#!/usr/bin/env bash 

PROJNAME="testSparkleRelease"

# create archive
xcodebuild clean archive -project $PROJNAME.xcodeproj -scheme $PROJNAME -archivePath $PROJNAME
# export archive to app
xcodebuild -exportArchive -archivePath "$PROJNAME.xcarchive" -exportPath Release -exportOptionsPlist "Release/ExportOptions.plist"

# cleanup
rm -R $PROJNAME.xcarchive
rm Release/DistributionSummary.plist
rm Release/Packaging.log
