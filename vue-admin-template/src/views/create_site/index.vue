<template>

  <el-form ref="form" :model="form" label-width="100px" >
    <el-form-item label="站点名称">
      <el-input placeholder="示例值：site" v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="站点描述">
      <el-input placeholder="示例值：site"v-model="form.description"></el-input>
    </el-form-item>
    <el-form-item label="	站点类型">
      <!--<el-input placeholder='示例值：["AP"] 混合站点类型集合：默认为AP。可选“AR”、“AP”、“FW”、“AC（Fit AP）”、“LSW”、“ONT”或者“OLT”中一个或多个类型。'v-model="form.type"></el-input>
      -->
      <el-select v-model="value1" multiple placeholder="请选择" size="medium">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="配置模式">
      <el-input placeholder="示例值：1 站点配置模式，取值范围为：1---默认，2---配置文件。"v-model="form.pattern"></el-input>
    </el-form-item>
    <el-form-item label="	纬度">
      <el-input placeholder="示例值：50 纬度，北纬是正数，南纬是负数，比如北纬30.2度，传入30.2,；南纬50.76度，传入-50.76，纬度范围【-90，+90】" v-model="form.latitude"></el-input>
    </el-form-item>
    <el-form-item label="经度">
      <el-input placeholder="示例值：111 经度，东经是正数，西经是负数，比如东经110度，传入110,；西经32.1度，传入-32.1，经度范围【-180，+180】"v-model="form.longtitude"></el-input>
    </el-form-item>
    <el-form-item label="联系人">
      <el-input placeholder="示例值：David"v-model="form.contact"></el-input>
    </el-form-item>
    <el-form-item label="标签">
      <el-input placeholder='示例值：["abcd"]'v-model="form.tag"></el-input>
    </el-form-item>
    <el-form-item label="是否隔离">
      <el-select v-model="value3" placeholder="请选择">
          <el-option
            v-for="item in options2"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="邮箱">
      <el-input placeholder="示例值：tenant@huawei.com"v-model="form.email"></el-input>
    </el-form-item>
    <el-form-item label="电话号码">
      <el-input placeholder="示例值：15277431823"v-model="form.phone"></el-input>
    </el-form-item>
    <el-form-item label="邮编">
      <el-input placeholder="示例值：215000"v-model="form.postcode"></el-input>
    </el-form-item>
    <el-form-item label="地址">
      <el-input placeholder="示例值：66 JiangYun Road"v-model="form.address"></el-input>
    </el-form-item>
    <el-form-item label="克隆站点ID">
      <el-input placeholder="示例值：ea25fdbf-8dee-4823-bac2-5bfe8e3359ca"v-model="form.cfgOriginId"></el-input>
    </el-form-item>
    <el-form-item label="克隆模式">
      <el-input placeholder="示例值：DEFAULT"v-model="form.cfgOriginType"></el-input>
    </el-form-item>
    <el-form-item label="克隆设备">
      <el-select v-model="value4" placeholder="请选择">
          <el-option
            v-for="item in options2"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
      </el-select>
    </el-form-item>


    <el-button style="margin-left: 20px" type="primary" @click="saveSite">保存站点信息</el-button>
    <el-button>取消</el-button>
    <p></p>

    <el-transfer :titles="['站点列表', '选择站点']" style="margin-left: 20px" v-model="value" :data="data" ></el-transfer>
    <p></p>

    <el-button style="margin-left: 20px" type="primary" @click="onSubmit">立即创建</el-button>
    <el-button>取消</el-button>

  </el-form>



</template>

<script>
import {CreateSite } from "@/api/createSite.js";

import  axios from 'axios'			//引入axios
  export default {
    data() {

      return {
        form: {
          name: '',
          description: '',
          type: '["AP"]',
          pattern: 1,
          latitude: '',
          longtitude: '',
          contact: '',
          tag: '["abcd"]',
          isolated: "false",
          email:'',
          phone:'',
          postcode:'',
          address:'',
          cfgOriginId: '',
          cfgOriginType:'',
          cloneDevices:"false"
        },
        data: [],
        value: [],
        siteList:[],
        SelectSite:[],
        name:[],
        options: [{
          value: 'AP',
          label: 'AP'
        }, {
          value: 'AR',
          label: 'AR'
        }, {
          value: 'FW',
          label: 'FW'
        }, {
          value: 'AC',
          label: 'AC'
        }, {
          value: 'LSW',
          label: 'LSW'
        }, {
          value: 'ONT',
          label: 'ONT'
        }, {
          value: 'OLT',
          label: 'OLT'
        }
        ],
        value1:[],
        options2: [{
          value: 'true',
          label: 'true'
        }, {
          value: 'false',
          label: 'false'
        }],
        //value3 是指isolated  value4是指cloneDevices
        value3:'',
        value4:''
      }
    },
    methods: {
      onSubmit() {

        this.SelectSite = [];
        for (let i =0; i<this.value.length;i++){
          this.SelectSite.push(this.siteList[this.value[i]])
        }
        console.log('SelectSite!', this.SelectSite);
        let p ={
          "sites":this.SelectSite
        }
        var formData = new FormData();
        formData.append('sites', JSON.stringify(this.SelectSite));
        console.log('p!', p);

        CreateSite(formData).then((res) => {
          console.log("res.success", res.success);
          console.log("res.errcode", res.errcode);
          console.log("res.errmsg", res.errmsg);
          console.log("res.fail", res.fail);

          this.$message({
              message: '恭喜你，站点创建成功',
              type: 'success'
        });
        });
        // $.ajax({
        //     type: "post",
        //     url: 'http://localhost:8000/api/create_site/',
        //     async: false, // 使用同步方式
        //     // 1 需要使用JSON.stringify 否则格式为 a=2&b=3&now=14...
        //     // 2 需要强制类型转换，否则格式为 {"a":"2","b":"3"}
        //     data: q,
        //     //请求头部设置
        //     contentType: "application/json; charset=utf-8",
        //     dataType: "json",
        //     success: function(data) {
        //         $('#chauncey').text(data.msg);
        //     }
        // });
      },
      saveSite(){
        console.log("this.value1", this.value1)
        this.form["type"] = JSON.stringify(this.value1)
        this.form["isolated"] = this.value3
        this.form["cloneDevices"] = this.value4
        this.name.push(this.form["name"]);
        this.siteList.push(this.form);
        console.log("this.name", this.name);
        console.log("this.form[\"type\"]", this.form["type"]);
        console.log(typeof this.form["type"])
        console.log("value", this.value);
        const data = [];
        for (let i = 0; i < this.siteList.length; i++) {
          data.push({
            key: i,
            label: `${ i }、${this.name[i]}`,
          });
        }
        this.data = data;
        // 重置表单
        this.form = this.$options.data().form;
      },

    }
  }
</script>
