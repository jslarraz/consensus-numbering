# consensus-numbering
A repository to test GitHub actions

## How to use this (it runs all on GitHub)
- Create a branch
- Put your candidate file in the candidate directory. Use the filename `candidate-usn`.
- Use `{{USN}}` in the contents to have it replaced by the assigned number upon merge.
- Create a PR. You can make any and all changes to the branch, the action only runs when the PR is merged into main.
- Approve the PR and see how the action computes the next number and makes all necessary changes.
