import request from "@/utils/request";
import axios from "axios";


export function CreateSite(params) {
  console.log("here is createsite", params)
  return request({
    url: '/api/create_site/',
    method: 'post',
    data: params,
    headers: {
        'Content-Type': 'application/json'
      },
  })
}

// export function CreateSite(parameter) {
//
//     return axios({
//       url: '/api/create_site/',
//       method: 'post',
//       data: JSON.stringify(parameter),
//       headers: {
//         'Content-Type': 'application/json'
//       },
//     })
//   }
