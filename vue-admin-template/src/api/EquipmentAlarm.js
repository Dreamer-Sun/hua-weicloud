import request from "@/utils/request";


export function equipmentAlarm(params) {
  console.log("here is equipmentAlarm api", params)
  return request({
    url: '/api/getEquipmentAlarm/',
    method: 'post',
    params
  })
}

export function getSiteId() {
  console.log("here is getSiteId api")
  return request({
    url: '/api/getSiteId',
    method: 'get',
  })
}
