<template>
  <div class="app-container">
    <el-button
      type="primary"
      >站点总数</el-button>
    {{siteNum}}
    <p></p>
    <el-input v-model="filterText" placeholder="Filter keyword" style="margin-bottom:30px;" />

    <el-tree
      ref="tree2"
      :data="tableData"
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
      siteNum :'',
      filterText: '',
      tableData:[],
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
    filterNode(value, data, node) {
      //查询显示当前节点
      /*if (!value) return true;
      return data.label.indexOf(value) !== -1;*/
      console.log(value, data, node)
	  //如果共有三级菜单，查询显示当前节点及所有子节点
      if (!value) return true;
      let if_one = data.label.indexOf(value) !== -1;
      let if_two =
        node.parent &&
        node.parent.data &&
        node.parent.data.label &&
        node.parent.data.label.indexOf(value) !== -1;
      let if_three =
        node.parent &&
        node.parent.parent &&
        node.parent.parent.data &&
        node.parent.parent.data.label &&
        node.parent.parent.data.label.indexOf(value) !== -1;
      let result_one = false;
      let result_two = false;
      let result_three = false;
      if (node.level === 1) {
        result_one = if_one;
      } else if (node.level === 2) {
        result_two = if_one || if_two;
      } else if (node.level === 3) {
        result_three = if_one || if_two || if_three;
      }
      return result_one || result_two || result_three;
    },
    GetData(){
        getSiteData().then((res) => {
          console.log(res.data)
          this.tableData = res.data;
          this.siteNum = res.totalRecords;
          console.log(this.tableData)
        });
    }
  }
}
</script>

