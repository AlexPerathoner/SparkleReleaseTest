# SparkleReleaseTest

WIP

Test repository to create a GitHub Action which

1. build xcode project
2. export app
3. sign app
4. create new github release with that app
5. -> should update rss feed used by Sparkle, which will trigger an automatic update on all devices which have already installed it

Todo: 
- [x] /release command triggers action and release
- [ ] signing not working
- [ ] update version in project