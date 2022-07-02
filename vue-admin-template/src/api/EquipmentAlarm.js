import request from "@/utils/request";



export function equipmentAlarm(params) {
  console.log("here is equipmentAlarm api", params)
  return request({
    url: '/api/getEquipmentAlarm/',
    method: 'post',
    data: params,
    headers: {
        'Content-Type': 'application/json'
      },
  })
}


export function equipmentAlarm2(params) {
  console.log("here is equipmentAlarm2 api", params)
  return request({
    url: '/api/getEquipmentAlarm2/',
    method: 'post',
    data: params,
    headers: {
        'Content-Type': 'application/json'
      },
  })
}
export function getSiteId() {
  console.log("here is getSiteId api")
  return request({
    url: '/api/getSiteId',
    method: 'get',
  })
}
