package com.kxjiang.blog.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.util.Date;
import lombok.Data;

/**
 * @author: Jiang
 * @createTime: ${Date} 22:31
 * @description: 
 */
/**
    * 博文信息表
    */
@ApiModel(value="com-kxjiang-blog-entity-TArticles")
@Data
@TableName(value = "t_articles")
public class TArticles {
    /**
     * 博文编号
     */
    @TableId(value = "article_id", type = IdType.AUTO)
    @ApiModelProperty(value="博文编号")
    private Integer articleId;

    /**
     * 博文标题
     */
    @TableField(value = "article_title")
    @ApiModelProperty(value="博文标题")
    private String articleTitle;

    /**
     * 博文简介
     */
    @TableField(value = "article_introduce")
    @ApiModelProperty(value="博文简介")
    private String articleIntroduce;

    /**
     * 博文内容表
     */
    @TableField(value = "article_content")
    @ApiModelProperty(value="博文内容表")
    private String articleContent;

    /**
     * 博文被查看次数
     */
    @TableField(value = "article_views")
    @ApiModelProperty(value="博文被查看次数")
    private Long articleViews;

    /**
     * 博文被查看次数统计
     */
    @TableField(value = "article_comment_count")
    @ApiModelProperty(value="博文被查看次数统计")
    private Long articleCommentCount;

    /**
     * 博文发表时间
     */
    @TableField(value = "article_date")
    @ApiModelProperty(value="博文发表时间")
    private Date articleDate;

    @TableField(value = "article_like_count")
    @ApiModelProperty(value="")
    private Long articleLikeCount;

    /**
     * 博文所属用户id
     */
    @TableField(value = "user_id")
    @ApiModelProperty(value="博文所属用户id")
    private Integer userId;

    public static final String COL_ARTICLE_ID = "article_id";

    public static final String COL_ARTICLE_TITLE = "article_title";

    public static final String COL_ARTICLE_INTRODUCE = "article_introduce";

    public static final String COL_ARTICLE_CONTENT = "article_content";

    public static final String COL_ARTICLE_VIEWS = "article_views";

    public static final String COL_ARTICLE_COMMENT_COUNT = "article_comment_count";

    public static final String COL_ARTICLE_DATE = "article_date";

    public static final String COL_ARTICLE_LIKE_COUNT = "article_like_count";

    public static final String COL_USER_ID = "user_id";
}