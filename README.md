# Data Structures and Algorithms Prep

---

## About this repository
This is a repository by Abhay Chauhan and Desh Iyer for practice data structures and algorithms in C++.

## Table of Contents

- [Data Structures and Algorithms Prep](#data-structures-and-algorithms-prep)
  - [About this repository](#about-this-repository)
  - [Table of Contents](#table-of-contents)
  - [Contributing to Public Repositories](#contributing-to-public-repositories)
    - [Getting Started](#getting-started)
    - [Creating a Pull Request (PR)](#creating-a-pull-request-pr)
    - [Updating the Clone](#updating-the-clone)
    - [Deleting a Branch](#deleting-a-branch)

## Contributing to Public Repositories

### Getting Started

1. Fork the repository you want to contribute to using the fork button on GitHub.
2. Go to your forked repository on github and clone it to your local machine using the following command,
    ```bash
    git clone <parent_repo_link> 
    ```
    For this example, let's say the repository's name is `test`.
3. Go to powershell and access the cloned repository with,
   ```bash
   cd test/

   // Open with VSCode
   code . 
   ```
4. Create a new local branch named `dev` on your cloned repository using,
   ```bash
   git checkout -b dev
   ```
   *Tip: To view all branches of the repository (local and remote) use,*
   ```bash
   git branch -a
   ```
   *To just view the remote branches use,*
   ```bash
   git branch -r
   ```
5. Connect the local branch to an upstream using the following command, 
   ```bash
   // We link our local branch to the parent repository by adding the parent repository as upstream
   git remote add upstream <link_to_parent_repository> 
   ```
6. Create necessary changes in the files, add and commit them using the normal git workflow with,
   ```
   git add .
   git commit -m "<your_commit_message>"
   ```
7. Push all the commits you've made on the `dev` branch using,
   ```bash
   git push origin dev
   ```
   This command not only pushes the changes to your branch, it also publishes your local branch to your remote forked repository. Now it should show up as a different branch in the branches dropdown on GitHub.

### Creating a Pull Request (PR)

Once your happy with the changes on your branch, you can push all the changes in your repository to the parent repository with a pull request. You need to go to the parent repository and create a pull request on the pull requests tab. The owner of the parent repository will then be able to merge your code to one of their branches and comment on the changes that you've made.

### Updating the Clone

To pull changes from the parent repository, change into the branch you want to pull changes into using,

```bash
git checkout dev
```

Then,
```
git fetch upstream
git merge upstream/main
```

*Note: Here, upstream/main refers to the main branch of the upstream repository, i.e., the parent repository.*

If you need to update a different branch, you need to checkout into that branch and run the commands to fetch and merge changes.

### Deleting a Branch

To delete a branch, make sure you checkout into a branch that isn't the one you need to delete. Then, you need to first delete the local and the remote instances with,

```bash
git branch --delete dev
git push origin --delete dev
```


---