# SparkleReleaseTest

WIP

Test repository to create a GitHub Action which

1. Owner comments `/release` on a PR to `master`, the workflow will:
1. Extrapolate from the file `Release_notes.md` the latest version number, the previous version number and the release notes
2. All occurences of the previous version number will be replaced with the new version number
1. The xcode project is archived and exported as an app (signing necessary, see [here](https://docs.github.com/en/actions/deployment/deploying-xcode-applications/installing-an-apple-certificate-on-macos-runners-for-xcode-development))
3. Zip app
3. Creating html file with release notes, with the same name as the app (needed by Sparkle)
5. Importing Sparkle private key from GitHub Secrets
4. Running the `generate_appcast` tool from Sparkle with that key to create/update the appcast.xml file in the Docs/Support folder
5. Creating GitHub release with the zipped apped, the release notes and the given version
6. Merging the PR, which updates the Docs/Support/appcast.xml, ued by GitHub Pages, which will trigger an automatic update on all devices which have already installed the app (in the `info.plist` file, the `SUFeedURL` key is set to a url which points to this file, see [here](https://sparkle-project.org/documentation/))

Todo: 
- [x] /release command triggers action and release
- [ ] signing not working
- [x] update version in project
- [ ] if MR failed, don't release new version
- [ ] if MR failed, downgrade version in project

## Important links

* https://sparkle-project.org/documentation/
* https://docs.github.com/en/actions/deployment/deploying-xcode-applications/installing-an-apple-certificate-on-macos-runners-for-xcode-development