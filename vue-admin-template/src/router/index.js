import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'
import path from "path";

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: 'Dashboard', icon: 'dashboard' }
    }]
  },

  {
    path: '/Sitedata_process',
    component: Layout,
    redirect: '/Sitedata_process/alarm',
    name: 'Sitedata_process',
    meta: { title: '站点数据处理', icon: 'el-icon-s-help' },
    children: [
      {
        path: 'alarm',
        name: 'alarm',
        component: () => import('@/views/alarm/index'),
        meta: { title: '告警设备查询', icon: 'table' }
      },
      {
        path: 'site_query',
        name: 'site_query',
        component: () => import('@/views/site_query/index'),
        meta: { title: '站点查询修改及删除', icon: 'tree' }
      },
      {
        path: 'create_site',
        name: 'create_site',
        component: () => import('@/views/create_site/index'),
        meta: { title: '创建站点', icon: 'tree' }
      },
      {
        path: 'mapshow',
        name: 'mapshow',
        component: () => import('@/views/mapshow/index'),
        meta: { title: '数据可视化', icon: 'tree'}
      }
    ]
  },
  {
    path: '/Device_management',
    component: Layout,
    redirect: '/Device_management/device_manage',
    name: 'Device_management',
    meta: { title: '设备处理', icon: 'el-icon-s-help' },
    children: [
      {
        path: 'device_manage',
        name: 'device_manage',
        component: () => import('@/views/test/index'),
        meta: {title: '站点设备管理', icon: 'tree'}
      },
      {
        path: 'device_manage2',
        name: 'device_manage2',
        component: () => import('@/views/test/traffic_monitoring'),
        meta: {title: '设备网络速率', icon: 'tree'}
      },
      // {
      //   path: 'device_manage3',
      //   name: 'device_manage3',
      //   component: () => import('@/views/test/traffic_monitoring'),
      //   meta: {title: '智能分析', icon: 'tree'}
      // }
    ]
  },

  {
    path: '/Traffic_statistics',
    component: Layout,
    name: 'Traffic_statistics',
    redirect: '/Traffic_statistics/traffic_statistics',
    meta: { title: '流量统计', icon: 'form' },
    children: [
      {
        path: 'topApp',
        name: 'topApp',
        component: () => import('@/views/traffic_statistics/topApp'),
        meta: { title: 'TopN应用流量', icon: 'form' }
      },
      {
        path: 'historyFlow',
        name: 'historyFlow',
        component: () => import('@/views/traffic_statistics/historyFlow'),
        meta: { title: '客流量查询', icon: 'form' }
      }
    ]
  },


  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
