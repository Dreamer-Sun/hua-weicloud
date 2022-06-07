<template>
  <div class="app-container">
    <el-button
      type="primary"
      >站点总数</el-button>
    <p></p>
    <el-input v-model="filterText" placeholder="Filter keyword" style="margin-bottom:30px;" />

    <el-tree
      ref="tree2"
      :data="data2"
      :props="defaultProps"
      :filter-node-method="filterNode"
      class="filter-tree"
      default-expand-all
    />

  </div>
</template>

<script>
import {getSiteData } from "@/api/getSiteData.js";

export default {

  data() {
    return {
      filterText: '',
      data2: [{
        id: 1,
        label: '设备id 1 ',
        children: [{
          id: 4,
          label: 'tenantId',
          children: [{
            id: 9,
            label: 'Level three 1-1-1'
          }, {
            id: 10,
            label: 'Level three 1-1-2'
          }]
        }]
      },
        {
        id: 2,
        label: '设备id 2',
        children: [{
          id: 5,
          label: 'Level two 2-1'
        }, {
          id: 6,
          label: 'Level two 2-2'
        }]
      },
        {
        id: 3,
        label: '设备id  3',
        children: [{
          id: 7,
          label: 'Level two 3-1'
        }, {
          id: 8,
          label: 'Level two 3-2'
        }]
      }],
      defaultProps: {
        children: 'children',
        label: 'label'
      }
    }
  },
  watch: {
    filterText(val) {
      this.$refs.tree2.filter(val)
    }
  },
  created() {
    this.GetData();
  },

  methods: {
    filterNode(value, data) {
      if (!value) return true
      return data.label.indexOf(value) !== -1
    },
    GetData(){

    }
  }
}
</script>

