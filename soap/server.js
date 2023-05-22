var express = require('express')
var soap = require('soap')
var app = express()

var tasks = []

var service = {
  TaskService: {
    TaskPort: {
      addTask: function(args) {
        var task = {
          title: args.task.title,
          description: args.task.description
        }
        tasks.push(task)
        return { addTaskResponse: { taskId: tasks.length } }
      },
      getTasks: function() {
        return { getTasksResponse: { tasks: tasks } }
      }
    }
  }
}

var xml = require('fs').readFileSync('tasks.wsdl', 'utf8');

app.use(express.static('public'))

app.listen(3000, function () {
  soap.listen(app, '/tasks', service, xml)
})
