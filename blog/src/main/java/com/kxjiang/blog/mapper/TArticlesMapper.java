package com.kxjiang.blog.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.kxjiang.blog.entity.TArticles;
import java.util.List;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

/**
 * @author: Jiang
 * @createTime: ${Date} 22:31
 * @description: 
 */
@Mapper
public interface TArticlesMapper extends BaseMapper<TArticles> {
    int updateBatch(List<TArticles> list);

    int updateBatchSelective(List<TArticles> list);

    int batchInsert(@Param("list") List<TArticles> list);

    int insertOrUpdate(TArticles record);

    int insertOrUpdateSelective(TArticles record);
}