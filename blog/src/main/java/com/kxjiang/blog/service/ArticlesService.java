package com.kxjiang.blog.service;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.kxjiang.blog.entity.TArticles;
import com.kxjiang.blog.mapper.TArticlesMapper;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.List;

/**
 * @author: Jiang
 * @createTime: 2021-04-07 19:14
 * @description:
 */
@Service
public class ArticlesService {
    @Resource
    TArticlesMapper tArticlesMapper;

    public List<TArticles> getArticles(String userId,String articleId,String articleTitle){
        LambdaQueryWrapper<TArticles> lambdaQueryWrapper = new LambdaQueryWrapper<>();
        lambdaQueryWrapper.eq(TArticles::getArticleId,articleId)
                .or().like(TArticles::getArticleTitle,articleTitle)
                .or().eq(TArticles::getUserId,userId);
        return tArticlesMapper.selectList(lambdaQueryWrapper);
    }
}
