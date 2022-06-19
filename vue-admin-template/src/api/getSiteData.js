import request from "@/utils/request";

export function getSiteData() {
  // console.log("此处可以用getSite")
  return request({
    url: '/api/getSiteData',
    method: 'GET'
  })
}

export function getsitemap() {
  return request({
    url: '/api/getsitemap',
    method: 'GET'
  })
}

export function getsitetypedata() {
  return request({
    url: '/api/getsitetypedata',
    method: 'GET'
  })
}

export function queryresultbyquerysitesdata() {
  return request({
    url: '/api/queryresultbyquerysitesdata',
    method: 'GET'
  })
}
