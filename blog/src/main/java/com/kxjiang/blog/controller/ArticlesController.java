package com.kxjiang.blog.controller;

import cn.hutool.core.util.StrUtil;
import com.kxjiang.blog.entity.TArticles;
import com.kxjiang.blog.service.ArticlesService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiImplicitParams;
import io.swagger.annotations.ApiOperation;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;
import java.net.http.HttpResponse;
import java.util.List;

/**
 * @author: Jiang
 * @createTime: 2021-04-07 17:48
 * @description:
 */
@RestController
@Api(tags = "博文表相关接口")
@RequestMapping("/articles")
public class ArticlesController {

    @Resource
    ArticlesService articlesService;

    @GetMapping(value = "/getArticles")
    @ApiImplicitParams({
            @ApiImplicitParam(name ="userId",value = "所属用户id",dataTypeClass = String.class,example = "1"),
            @ApiImplicitParam(name ="articleId",value = "博文id",dataTypeClass = String.class,example = "1"),
            @ApiImplicitParam(name ="articleTitle",value = "博文标题",dataTypeClass = String.class ,example = "oracle")
    })
    @ApiOperation(value = "查询博文表信息",notes = "查询博文表信息")
    public List<TArticles> getArticles(String userId, String articleId, String articleTitle){
        if(StrUtil.isBlank(userId)) userId = "";
        if(StrUtil.isBlank(articleId)) articleId = "";
        if(StrUtil.isBlank(articleTitle)) articleTitle = "";
        /*TArticles tArticles = new TArticles();
        tArticles.setUserId(1);*/
        TArticles tArticles = new TArticles();

        return articlesService.getArticles(userId, articleId, articleTitle);
    }
}
