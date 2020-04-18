# C++ Torch指北

### 安装

 - Windows 下的 torch c++ 安装
   	
   	- 首先在torch 官网下载安装包， debug 与 release均可，windows 尽量下载debug版本
   - 编译时候的配置：
   - 如果下载的是GPU版本的，需要下载对应cuda版本的pytorch-gpu（地址同样在pytorch 官网）

### 项目编译

   	  - 然后编辑CmakeLists.txt即可，下面给出一段 cmake 文件的示例
   
   	  - ```bash
      	    cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
      	    project(example-app)
      	    SET(Torch_DIR C:/ProgramData/Anaconda3/Lib/site-packages/torch/share/cmake/Torch) # pytorch location
      	    SET(TORCH_LIBRARIES C:/libtorch) # torchlib location
      	    find_package(Torch REQUIRED)
      	    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")
      	    add_executable(example-app main.cpp)
      	    target_link_libraries(example-app "${TORCH_LIBRARIES}")
      	    set_property(TARGET example-app PROPERTY CXX_STANDARD 14)
      	    
      	    if (MSVC)
      	      file(GLOB TORCH_DLLS "${TORCH_INSTALL_PREFIX}/lib/*.dll")
      	      add_custom_command(TARGET example-app
      	                         POST_BUILD
      	                         COMMAND ${CMAKE_COMMAND} -E copy_if_different
      	                         ${TORCH_DLLS}
      	                         $<TARGET_FILE_DIR:example-app>)
      	    endif (MSVC)
   ```

   	  - 编译链接的时候不要使用 vs，使用cmake即可，且编译出的vs项目文件（.sln）无法被VS正常编译运行（windows 下只能使用cmake 进行原生编译）
   
   	  - ```bash
      	    mmkdir build
   cd build
   cmake -DCMAKE_GENERATOR_PLATFORM=x64  ..
   cmake --build . --config Release
   ```


   	

- 多个Cpp 文件的同时编译

  - ```bash
    cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
    project(example-app)
    SET(Torch_DIR E:/Anaconda/Lib/site-packages/torch/share/cmake/Torch) # pytorch location， CUDA 的对应版本要与torchlib 一致
    SET(TORCH_LIBRARIES C:/libtorch) # torchlib location
    
    find_package(Torch REQUIRED)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")
    
    # add all cpp file to exe 
    include_directories("${PROJECT_BINARY_DIR}")
    
    # Find all main*.cpp files and store in list mains
    file(GLOB_RECURSE mains RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}" "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp")
    foreach(mainfile IN LISTS mains)
        # Get file name without directory
        get_filename_component(mainname ${mainfile} NAME_WE)
        add_executable(${mainname} ${mainfile})
        target_link_libraries(${mainname} "${TORCH_LIBRARIES}")
        set_property(TARGET ${mainname} PROPERTY CXX_STANDARD 14)
        if (MSVC)
        	file(GLOB TORCH_DLLS "${TORCH_INSTALL_PREFIX}/lib/*.dll")
            add_custom_command(TARGET ${mainname}
                         POST_BUILD
                         COMMAND ${CMAKE_COMMAND} -E copy_if_different
                         ${TORCH_DLLS}
                         $<TARGET_FILE_DIR:${mainname}>)
    	endif (MSVC)
    endforeach()
    ```

    