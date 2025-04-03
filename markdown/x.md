```mermaid
graph TD;
    A["输入: cf_vec (小波系数), dim_vec (尺寸矩阵)"] --> B["初始化 dn = 3"];
    B --> C["计算 num = (length(cf_vec) - 1) / dn"];
    C --> D["提取初始低频系数 tmpa = wkeep(cf_vec{1}, dim_vec(1,:), 'c')"];
    D --> E["归一化 tmpa 并转换为 uint8"];
    E --> F["设置 tmpa 边界像素为 255"];
    
    F --> G["循环处理每层小波系数"];
    G --> H["提取纵向高频 tmpv, 水平高频 tmph, 对角高频 tmpd"];
    H --> I["归一化 tmpv, tmph, tmpd 并转换为 uint8"];
    I --> J["设置 tmpv, tmph, tmpd 的边界像素为 255"];
    
    J --> K["拼接 tmp = [tmpa, tmpv; tmph, tmpd]"];
    K --> L["调整尺寸: 根据 dim_vec(j+1, :) 截取 tmpa"];
    L --> M["归一化 tmpa 并设置边界像素为 255"];
    
    M --> G["继续下一层处理 (直到所有层处理完毕)"];
    M --> N["绘制最终小波系数塔式图"];
    N --> O["显示图像 imshow(tmpa, []) 并设置标题"];
