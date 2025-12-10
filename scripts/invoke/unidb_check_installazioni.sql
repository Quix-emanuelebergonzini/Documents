SELECT cod_installazione, TIMESTAMPDIFF(YEAR, modificato, CURDATE()) AS diff
FROM pos_install_packages
WHERE 1 AND update_type = 'db' AND creation_mode = 'full'
HAVING diff > 1
ORDER BY id DESC;