<template>
  <div id="app">
    {{msg}}

    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <input type="text" class="form-control col-3 mx-2" placeholder="Name" v-model="student.StudName">
        <input type="text" class="form-control col-3 mx-2" placeholder="Course" v-model="student.Course">
        <input type="text" class="form-control col-3 mx-2" placeholder="Rating" v-model="student.Rating">
        <button class="btn btn-success">Submit</button>
      </div>
    </form>
    

    <table class="table">
      <thead>
        <th>Name</th>
        <th>Course</th>
        <th>Rating</th>
      </thead>
      <tbody>
        <tr v-for="student in students" :key="student.id" @dblclick="$data.student = 
        student">
          <td>{{student.StudName}}</td>
          <td>{{student.Course}}</td>
          <td>{{student.Rating}}</td>
          <td>
            <button class="btn btn-outline-danger btn sm mx-1" 
            @click="deleteStudent(student)">X</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>

export default {
  name: 'App',
  data(){
    return {
      msg: 'system test',
      students: [],
      student: {},
    }
  },
  async created(){
    await this.getStudentes();
  },
  methods: {
    submitForm(){
      if (this.student.StudId == undefined){
        this.createStudent();
      } else {
        this.editStudent();
      }
    },
    async getStudentes(){
      var response = await fetch('http://127.0.0.1:8000/api/students/')
      this.students = await response.json();
    },
    async createStudent(){
      await this.getStudentes();
      await fetch('http://127.0.0.1:8000/api/students/', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student)
      });
      await this.getStudentes();
    },
    async editStudent(){
      await this.getStudentes();
      await fetch(`http://127.0.0.1:8000/api/students/${this.student.StudId}/`, {
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student)
      });
      await this.getStudentes();
      this.student = {};
    },
    async deleteStudent(student){
      await this.getStudentes();
      await fetch(`http://127.0.0.1:8000/api/students/${student.StudId}/`, {
        method: 'delete',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student)
      });
      await this.getStudentes();
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
