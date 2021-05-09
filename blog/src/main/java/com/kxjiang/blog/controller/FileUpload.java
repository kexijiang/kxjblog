package com.kxjiang.blog.controller;

import cn.hutool.core.util.IdUtil;
import cn.hutool.log.Log;
import com.kxjiang.blog.entity.api.R;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import javax.annotation.Resource;
import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 作者: Jiang
 * 创建时间: 2021-04-19 10:32
 * 描述:
 */
@RestController
@RequestMapping(value = "/file")
@Api(tags = "文件上传")
public class FileUpload {

    @Resource
    RedisTemplate<String,String> redisTemplate;

    static final Log logger = Log.get();
    private String filePath;

    @Value("${config.file.url}")
    public void setFilePath(String filePath) {
        this.filePath = filePath;
    }

    @RequestMapping(value = "/upload", method = {RequestMethod.POST},consumes = "multipart/*",headers = "content-type=multipart/form-data")
    @ApiOperation(value = "文件上传")
    @ApiImplicitParam(paramType = "form",dataType = "__file",name = "files",value = "files")
    public R<List<Map<String,String>>> upload(@RequestParam(value = "files") MultipartFile[] files) {
        try {
            List<Map<String,String>> resultList = new ArrayList<>();
            for (MultipartFile file:files) {
                Map<String,String> resultMap = uploadFile(file);
                resultList.add(resultMap);
            }
            return new R<List<Map<String,String>>>().data(resultList);
        } catch (Exception var3) {
            return new R<>(var3.getMessage());
        }
    }
    public Map<String,String> uploadFile(MultipartFile file) throws Exception {
        Map<String,String> resultMap = new HashMap<>();
        String shortPath =  file.getOriginalFilename();
        assert shortPath != null;
        String filePathName = filePath+shortPath;
        resultMap.put("filePath",filePathName);


        String key = IdUtil.simpleUUID();
        redisTemplate.boundValueOps(key).set(filePathName);
        logger.info("保存redis成功!key->{},value->{}",key,filePathName);
        File dest = new File(filePathName);
        if (!dest.getParentFile().exists()) {
            boolean rel = dest.getParentFile().mkdirs();
            if (!rel) {
                throw new Exception("文件夹创建失败");
            }
        }
        try (InputStream is = file.getInputStream(); OutputStream os = new FileOutputStream(dest)) {
            byte[] buffer = new byte[8 * 1024];
            int bytesRead;
            while ((bytesRead = is.read(buffer)) != -1) {
                os.write(buffer, 0, bytesRead);
            }
        }
        resultMap.put("message","上传成功！");
        return resultMap;
    }
}
