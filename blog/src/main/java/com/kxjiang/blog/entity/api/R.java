package com.kxjiang.blog.entity.api;

import io.swagger.annotations.ApiModel;
import lombok.Data;

/**
 * 作者: Jiang
 * 创建时间: 2021-04-24 23:41
 * 描述: http请求公共返回参数实体类
 */
@Data
@ApiModel
public class R<T> {
    private String code;
    private String message;
    private T data;

    public R() {
    }

    public R(T data) {
        this.data = data;
    }

    public R(String code, T data) {
        this.code = code;
        this.data = data;
    }

    public R(String code, String message, T data) {
        this.code = code;
        this.message = message;
        this.data = data;
    }

    public R<T> data(T t){
        return new R<>("200","成功",t);
    }

    public R(String message) {
        this.message = message;
    }

}
