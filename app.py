from flask import Flask, render_template, request
import git

##############################

# https://---GITHUB_TOKEN_HERE---@github.com/---GITHUB_USERNAME_NAME---/mysite.git

app = Flask(__name__)

@app.post('/SECRET-URL-HERE')
def git_update():
  repo = git.Repo('./mysite')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""


##############################
@app.get("/")
def index():
  return "x"
