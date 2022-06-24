import request from "@/utils/request";

export function getdeviceinfo(params) {
  // console.log("此处可以用showtoken")
  return request({
    url: '/api/getdeviceinfo',
    method: 'GET',
    params
  })
}

export function createdevice(params) {
  // console.log("此处可以用createdevice", params)
  return request({
    url: '/api/createdevice/',
    method: 'post',
    params,
      headers: {
        'Content-Type': 'application/json'
      },
  })
}

export function deletedevice(params) {
  // console.log("此处可以用deletedevice", params)
  return request({
    url: '/api/deletedevice/',
    method: 'delete',
    params,
      headers: {
        'Content-Type': 'application/json'
      },
  })
}
