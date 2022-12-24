<template>
    <div 
    :class="[statusAtivo ? 'ativo' : 'desativado']"></div>
</template>

<script>
export default{
  props:{
    statusAtivo:{
      type: Boolean,
      default: false
    }
  },

  methods:{
    
  }
}
</script>

<style>

.ativo{
  background-color: green;
}

.desativado{
  background-color: rgb(196, 196, 196);
}

</style>

