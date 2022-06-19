<template>

  <el-form ref="form" :model="form" label-width="80px">
    <el-form-item label="站点名称">
      <el-input placeholder="示例值：site" v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="站点描述">
      <el-input placeholder="示例值：site"v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="	站点类型">
      <el-input placeholder='示例值：["AP"] 混合站点类型集合：默认为AP。可选“AR”、“AP”、“FW”、“AC（Fit AP）”、“LSW”、“ONT”或者“OLT”中一个或多个类型。'v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="配置模式">
      <el-input placeholder="示例值：1 站点配置模式，取值范围为：1---默认，2---配置文件。"v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="	纬度">
      <el-input placeholder="示例值：50 纬度，北纬是正数，南纬是负数，比如北纬30.2度，传入30.2,；南纬50.76度，传入-50.76，纬度范围【-90，+90】"v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="经度">
      <el-input placeholder="示例值：111 经度，东经是正数，西经是负数，比如东经110度，传入110,；西经32.1度，传入-32.1，经度范围【-180，+180】"v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="联系人">
      <el-input placeholder="示例值：David"v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="标签">
      <el-input placeholder='示例值：["abcd"]'v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="是否隔离">
      <el-input placeholder='示例值：["abcd"]'v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="邮箱">
      <el-input placeholder="示例值：tenant@huawei.com"v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="电话号码">
      <el-input placeholder="示例值：15277431823"v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="地址">
      <el-input placeholder="示例值：66 JiangYun Road"v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="克隆站点ID">
      <el-input placeholder="示例值：ea25fdbf-8dee-4823-bac2-5bfe8e3359ca"v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="克隆模式">
      <el-input placeholder="示例值：DEFAULT"v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="克隆设备">
      <el-input placeholder="示例值：false"v-model="form.name"></el-input>
    </el-form-item>


    <el-form-item>
      <el-button type="primary" @click="onSubmit">立即创建</el-button>
      <el-button>取消</el-button>
    </el-form-item>
  </el-form>

</template>

<script>
  export default {
    data() {
      return {
        form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        }
      }
    },
    methods: {
      onSubmit() {
        console.log('submit!');
      }
    }
  }
</script>
