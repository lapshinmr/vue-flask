<template>
  <div class="home">
    <HelloWorld :msg="msg"/>
    <v-btn @click="getMessage">
      Call server
    </v-btn>
  </div>
</template>

<script>
import axios from 'axios'
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  },
  data () {
    return {
      msg: ''
    }
  },
  methods: {
    getMessage () {
      const path = 'http://localhost:5000/api'
      axios.get(path)
        .then((res) => {
          this.msg = res.data
        })
        .catch((error) => {
          console.log(error)
          // eslint-disable-next-line
        })
    }
  }
}
</script>
