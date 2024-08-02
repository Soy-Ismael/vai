<?php include 'header.php'; ?>
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f2f2f2;
    }

    .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }

    .metric {
        background-color: white;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
</style>
    <main class="main">
        <h2 class="main__title">Panel Principal</h2>
        <!-- graphs and informations about the hardware and software of the host -->
        <!-- <p>Proximamente...</p> -->
        <?php
        $os = php_uname();
        $php_os = PHP_OS;
        $disk_total = disk_total_space("/");
        $disk_free = disk_free_space("/");

        // Obtener carga de CPU
        $cpu_load = shell_exec("wmic cpu get loadpercentage");
        $cpu_load = trim(explode("\n", $cpu_load)[1]);

        // Obtener información de memoria
        $memory_info = shell_exec("wmic OS get FreePhysicalMemory,TotalVisibleMemorySize");
        $memory_info = explode("\n", trim($memory_info));
        $free_memory = trim($memory_info[1]); // Memoria libre
        $total_memory = trim($memory_info[0]); // Memoria total
        ?>

        <div class="container">        
            <div class="metric">
                <h2>Sistema Operativo</h2>
                <p><?php echo $os; ?></p>
            </div>
            
            <div class="metric">
                <h2>PHP OS</h2>
                <p><?php echo $php_os; ?></p>
            </div>
            
            <div class="metric">
                <h2>Espacio en Disco</h2>
                <p><?php echo round($disk_free / (1024*1024*1024), 2); ?> GB / <?php echo round($disk_total / (1024*1024*1024), 2); ?> GB</p>
            </div>
            
            <div class="metric">
                <h2>Carga de CPU</h2>
                <p><?php echo $cpu_load; ?>%</p>
            </div>
        </div>
    </main>
<?php include 'imports.php' ?>