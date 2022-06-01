const API = {
    service: "",
    login: {
        url: "/api/login",
        method: "POST",
        token: !1,
        name: "登录",
    },
    logout: {
        url: "/api/logout",
        method: "POST",
        token: !0,
        name: "退出登录",
    },
    qrcode: {
        url: "/api/dupan/login/qrcode",
        method: "POST",
        token: !0,
        name: "获取登录二维码",
    },
    is_login: {
        url: "/api/dupan/login/is_login",
        method: "POST",
        token: !0,
        name: "是否登录"
    }

}

function request(settings) {
    let defaultSettings = {
        name: "",
        data: {},
        headers: {},
        async: false,
        success: (response) => {
        },
        error: (error) => {
        },
        callback: (response) => {
        }
    };
    $.extend(defaultSettings, settings)
    if (API[defaultSettings.name].token) {
        defaultSettings.headers['X-CSRFToken'] = $.cookie("csrftoken");
    }
    // if (defaultSettings.async) {
    //     return await new Promise(resolve => {
    //         resolve(
    //             axios.request({
    //                 url: API[defaultSettings.name].url,
    //                 data: defaultSettings.data,
    //                 method: API[defaultSettings.name].method,
    //                 headers: defaultSettings.headers,
    //             })
    //         );
    //     });
    // };
    return axios.request({
        url: API[defaultSettings.name].url,
        data: defaultSettings.data,
        method: API[defaultSettings.name].method,
        headers: defaultSettings.headers,
    })
        .then((response) => {
            defaultSettings.success(response);
        })
        .catch((error) => {
            defaultSettings.error(error);
        })
        .then(() => {
            defaultSettings.callback();
        })
}


