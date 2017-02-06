<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>vue + flask todos</h2>
    <ul>
      <li v-for="todo in todos">
        {{ todo.title }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'hello',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      todos: []
    }
  },
  mounted (){
      var o = this
      axios.get('/api/todos').then((response) => {
          o.todos = response.data
      })
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
