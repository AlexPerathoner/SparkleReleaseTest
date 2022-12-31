# SparkleReleaseTest

This is a example project to show how to create a GitHub Action to automatically create a release for a macOS app, using Sparkle.

## What does the workflow do?

The owner creates a PR to `master` and comments `/release`. If the PR is mergeable, this triggers a GitHub Action which will:
1. Extrapolate from the file `Release_notes.md` the:
    * latest version number
    * its release notes
    * its title
    * previous version number
1. Replace all occurences of the previous version number with the new version number within the Xcode project
1. Archive and export the Xcode project as a .app
4. Run the `generate_appcast` tool from Sparkle, which will create/update the appcast.xml file in the Docs/Support folder
5. Create a GitHub release with the zipped app, the release note, the latest version and the title
6. Merge the PR, which triggers the GitHub action to build GitHub Pages, which will host the `appcast.xml` file. The update is so available for all users.


## Necessary steps to make this work

* Add a private sparkle key to the GitHub secrets
* Add a build certificate and a provision profile to the GitHub secrets, see [here](https://docs.github.com/en/actions/deployment/deploying-xcode-applications/installing-an-apple-certificate-on-macos-runners-for-xcode-development) - needed in step 3
* Add a `Release_Notes.md` file to the root of the project, (look at [Release_Notes.md](Release_Notes.md) for an example of how the release notes should be formatted))])
* Add a `docs` folder to the root of the project, with a `Support` folder inside it. This is where the `appcast.xml` file will be generated and hosted.
* Set `docs` in the `master` branch as the GitHub Pages source (repository settings > pages > source)
* In the `info.plist` file of the Xcode project:
    * Set the `SUFeedURL` to `https://<username>.github.io/<repo>/Support/appcast.xml`
    * Set the `SUPublicEDKey` to the public key, see [here](https://sparkle-project.org/documentation/) on how to generate one
* In the Xcode project set the project and marketing versions to the same value (Project > General > Identity > Version and Build)
* Add an item in the Release_Notes.md file for the current version, with the title `# <version> - <title>`, e.g. `# 1.0.0 - Initial Release`, this will be used by the workflow to get the previous version number
* Create a Configuration folder and copy all the files from the `Configuration` folder in this repo to it
    * update `ExportOptions.plits` with your Team ID


## Important links

* https://sparkle-project.org/documentation/
* https://docs.github.com/en/actions/deployment/deploying-xcode-applications/installing-an-apple-certificate-on-macos-runners-for-xcode-development

### Useful links for creating the workflow

* https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#get-a-pull-request
* https://docs.github.com/en/actions/learn-github-actions/contexts#github-context
